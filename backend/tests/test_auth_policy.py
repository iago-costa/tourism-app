"""Auth policy: password only in development; Google in production."""

from __future__ import annotations

import os

import pytest
from httpx import ASGITransport, AsyncClient

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./tourism_policy_test.db"
os.environ["STRIPE_WEBHOOK_SECRET"] = "whsec_test"
os.environ["ENVIRONMENT"] = "development"

from app.config import settings  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(autouse=True)
def _restore_environment():
    original = settings.environment
    yield
    settings.environment = original


@pytest.mark.asyncio
async def test_auth_config_development():
    settings.environment = "development"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.get("/api/v1/auth/config")
    assert r.status_code == 200
    data = r.json()
    assert data["allow_password_auth"] is True
    assert data["social_oauth_per_user"] is False


@pytest.mark.asyncio
async def test_auth_config_production():
    settings.environment = "production"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.get("/api/v1/auth/config")
    assert r.status_code == 200
    assert r.json() == {"allow_password_auth": False}


@pytest.mark.asyncio
async def test_login_password_blocked_in_production():
    settings.environment = "production"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.post(
            "/api/v1/auth/login",
            json={"email": "dev@example.com", "password": "secret123"},
        )
    assert r.status_code == 403
    assert r.json()["detail"] == "Autenticação não disponível."


@pytest.mark.asyncio
async def test_register_password_blocked_in_production():
    settings.environment = "production"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.post(
            "/api/v1/auth/register",
            json={"email": "new@example.com", "password": "secret123", "full_name": "Test"},
        )
    assert r.status_code == 403
