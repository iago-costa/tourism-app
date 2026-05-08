import os
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import delete

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./tourism_test.db"
os.environ["STRIPE_WEBHOOK_SECRET"] = "whsec_test"

from app.database import AsyncSessionLocal, engine  # noqa: E402
from app.main import app  # noqa: E402
from app.models import Base, Subscription, User  # noqa: E402


@pytest.fixture(autouse=True)
async def reset_db():
    db_file = Path("tourism_test.db")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with AsyncSessionLocal() as session:
        await session.execute(delete(Subscription))
        await session.execute(delete(User))
        await session.commit()
    if db_file.exists():
        db_file.unlink()


@pytest.mark.asyncio
async def test_auth_flow():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        register = await client.post(
            "/api/v1/auth/register",
            json={"email": "test@tourism.com", "password": "secret123", "full_name": "Test User"},
        )
        assert register.status_code == 200

        login = await client.post("/api/v1/auth/login", json={"email": "test@tourism.com", "password": "secret123"})
        assert login.status_code == 200
        tokens = login.json()
        assert "access_token" in tokens
        assert "refresh_token" in tokens

        me = await client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {tokens['access_token']}"})
        assert me.status_code == 200
        assert me.json()["email"] == "test@tourism.com"

        refresh = await client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
        assert refresh.status_code == 200
        assert "access_token" in refresh.json()


@pytest.mark.asyncio
async def test_stripe_webhook_is_idempotent(monkeypatch):
    async with AsyncSessionLocal() as session:
        user = User(email="stripe@tourism.com", full_name="Stripe User", hashed_password="x")
        session.add(user)
        await session.flush()
        session.add(Subscription(user_id=user.id, status="checkout_created"))
        await session.commit()
        user_id = user.id

    def fake_construct_event(payload, sig_header, secret):  # noqa: ANN001
        return {
            "id": "evt_tourism_1",
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "metadata": {"user_id": str(user_id)},
                    "client_reference_id": str(user_id),
                    "customer": "cus_123",
                    "subscription": "sub_123",
                }
            },
        }

    from app.routes import billing

    monkeypatch.setattr(billing.stripe.Webhook, "construct_event", fake_construct_event)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        first = await client.post("/api/v1/billing/webhook", content=b"{}", headers={"stripe-signature": "sig"})
        assert first.status_code == 200
        assert first.json()["received"] is True

        second = await client.post("/api/v1/billing/webhook", content=b"{}", headers={"stripe-signature": "sig"})
        assert second.status_code == 200
        assert second.json().get("duplicate") is True
