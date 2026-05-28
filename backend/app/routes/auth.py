"""Authentication routes: password + Google OAuth + recovery."""

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db_session
from app.dependencies import get_current_user
from app.models import PasswordResetToken, RefreshToken, User
from app.services.email import send_password_reset_email
from app.services.google_oauth import build_google_authorize_url, fetch_google_profile
from app.services.security import create_access_token, create_refresh_token, decode_token, hash_password, verify_password
from app.services.tokens import generate_reset_token
from app.services.tokens import token_digest
from app.config import settings

router = APIRouter()

_PASSWORD_AUTH_DISABLED = (
    "Login por e-mail/senha disponível apenas em ambiente de desenvolvimento. Use Google."
)


def _require_password_auth() -> None:
    if not settings.allow_password_auth:
        raise HTTPException(status_code=403, detail=_PASSWORD_AUTH_DISABLED)


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str = ""


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirmRequest(BaseModel):
    token: str
    new_password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class AuthConfigResponse(BaseModel):
    """Public auth capabilities (no secrets)."""

    allow_password_auth: bool
    google_oauth_configured: bool
    social_oauth_per_user: bool = False


@router.get("/config", response_model=AuthConfigResponse)
async def auth_config() -> AuthConfigResponse:
    """Capabilities for login UI (password vs Google-only in production)."""
    return AuthConfigResponse(
        allow_password_auth=settings.allow_password_auth,
        google_oauth_configured=bool(settings.google_oauth_client_id),
        social_oauth_per_user=False,
    )


@router.post("/register")
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db_session)):
    _require_password_auth()
    """Register a new user account."""
    existing = await db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    await db.commit()
    return {"message": "User registered"}


@router.post("/login")
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db_session)):
    _require_password_auth()
    """Authenticate and return a JWT token."""
    user = await db.scalar(select(User).where(User.email == payload.email))
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(subject=user.email)
    refresh_token = create_refresh_token(subject=user.email)
    db.add(RefreshToken(user_id=user.id, token_hash=token_digest(refresh_token)))
    await db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.post("/refresh")
async def refresh_token(payload: RefreshRequest, db: AsyncSession = Depends(get_db_session)):
    """Issue a new access token from a refresh token."""
    token_hash = token_digest(payload.refresh_token)
    persisted = await db.scalar(select(RefreshToken).where(RefreshToken.token_hash == token_hash))
    if not persisted or persisted.is_revoked:
        raise HTTPException(status_code=401, detail="Refresh token revoked")
    try:
        decoded = decode_token(payload.refresh_token)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from exc
    if decoded.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")
    return {"access_token": create_access_token(subject=decoded["sub"]), "token_type": "bearer"}


@router.post("/logout")
async def logout(payload: RefreshRequest, db: AsyncSession = Depends(get_db_session)):
    """Revoke refresh token."""
    token_hash = token_digest(payload.refresh_token)
    persisted = await db.scalar(select(RefreshToken).where(RefreshToken.token_hash == token_hash))
    if persisted:
        persisted.is_revoked = True
        await db.commit()
    return {"message": "Logged out successfully"}


@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "oauth_provider": current_user.oauth_provider,
    }


@router.get("/google/start")
async def google_oauth_start():
    """Return Google OAuth authorization URL."""
    if not (build_google_authorize_url and fetch_google_profile):
        raise HTTPException(status_code=500, detail="OAuth service error")
    return {"provider": "google", "authorize_url": build_google_authorize_url()}


@router.api_route("/google/callback", methods=["GET", "POST"])
async def google_oauth_callback(
    request: Request,
    code: str | None = None,
    db: AsyncSession = Depends(get_db_session),
):
    """Google OAuth callback endpoint."""
    # Support both redirect-style (GET ?code=...) and API-driven (POST {"code": ...})
    if request.method == "POST":
        try:
            payload = await request.json()
        except Exception:
            payload = None

        if isinstance(payload, dict):
            code = payload.get("code") or payload.get("authorization_code") or code

        # Also tolerate application/x-www-form-urlencoded bodies.
        if not code:
            try:
                form = await request.form()
                if "code" in form:
                    code = form.get("code") or code
            except Exception:
                pass

    if not code:
        raise HTTPException(status_code=400, detail="Missing OAuth code")
    if not (build_google_authorize_url and fetch_google_profile):
        raise HTTPException(status_code=503, detail="Google OAuth is not configured")

    profile = await fetch_google_profile(code)
    email = profile.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Could not retrieve Google user email")
    user = await db.scalar(select(User).where(User.email == email))
    if not user:
        user = User(
            email=email,
            full_name=profile.get("name", ""),
            hashed_password=hash_password(generate_reset_token()),
        )
        user.oauth_provider = "google"
        db.add(user)
        await db.commit()
    token = create_access_token(subject=email)
    return {"message": "Google login successful", "access_token": token, "token_type": "bearer"}


@router.post("/recover-account")
async def recover_account(payload: PasswordResetRequest, db: AsyncSession = Depends(get_db_session)):
    _require_password_auth()
    """Trigger password reset email via Resend."""
    user = await db.scalar(select(User).where(User.email == payload.email))
    if not user:
        return {"message": "If account exists, recovery email was sent."}
    token = generate_reset_token()
    reset = PasswordResetToken(
        user_id=user.id,
        token_hash=token_digest(token),
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )
    db.add(reset)
    await db.commit()
    await send_password_reset_email(payload.email, token)
    return {"message": "If account exists, recovery email was sent."}


@router.post("/reset-password")
async def reset_password(payload: PasswordResetConfirmRequest, db: AsyncSession = Depends(get_db_session)):
    _require_password_auth()
    """Reset password with token sent by email."""
    hashed_token = token_digest(payload.token)
    reset = await db.scalar(select(PasswordResetToken).where(PasswordResetToken.token_hash == hashed_token))
    if not reset:
        raise HTTPException(status_code=400, detail="Invalid reset token")
    if reset.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Expired reset token")

    user = await db.scalar(select(User).where(User.id == reset.user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.hashed_password = hash_password(payload.new_password)
    await db.delete(reset)
    await db.commit()
    return {"message": "Password updated successfully"}
