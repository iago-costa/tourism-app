from fastapi import Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db_session
from app.models import User
from app.services.security import decode_token


async def get_current_user(
    authorization: str | None = Header(default=None),
    db: AsyncSession = Depends(get_db_session),
) -> User:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = authorization.split(" ", 1)[1].strip()
    try:
        decoded = decode_token(token)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Invalid access token") from exc
    if decoded.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")
    user = await db.scalar(select(User).where(User.email == decoded.get("sub", "")))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
