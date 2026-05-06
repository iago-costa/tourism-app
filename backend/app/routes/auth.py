"""Authentication routes — register, login, token refresh."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register():
    """Register a new user account."""
    return {"message": "Registration endpoint — TODO: implement"}


@router.post("/login")
async def login():
    """Authenticate and return a JWT token."""
    return {"message": "Login endpoint — TODO: implement"}


@router.post("/refresh")
async def refresh_token():
    """Refresh an expired access token."""
    return {"message": "Token refresh endpoint — TODO: implement"}
