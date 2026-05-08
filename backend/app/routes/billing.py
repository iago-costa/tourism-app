"""Stripe subscription routes."""

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, EmailStr
import stripe
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db_session
from app.dependencies import get_current_user
from app.models import Subscription, User, WebhookEvent

router = APIRouter()


class CheckoutRequest(BaseModel):
    customer_email: EmailStr


@router.post("/checkout")
async def create_checkout_session(payload: CheckoutRequest, db: AsyncSession = Depends(get_db_session)):
    """Create Stripe checkout session for monthly subscription."""
    if not settings.stripe_secret_key or not settings.stripe_price_monthly_id:
        raise HTTPException(status_code=503, detail="Stripe is not configured")

    stripe.api_key = settings.stripe_secret_key
    user = await db.scalar(select(User).where(User.email == payload.customer_email))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session = stripe.checkout.Session.create(
        mode="subscription",
        success_url=settings.stripe_success_url,
        cancel_url=settings.stripe_cancel_url,
        customer_email=payload.customer_email,
        client_reference_id=str(user.id),
        metadata={"user_id": str(user.id)},
        line_items=[{"price": settings.stripe_price_monthly_id, "quantity": 1}],
    )
    db.add(
        Subscription(
            user_id=user.id,
            stripe_customer_id=session.customer or "",
            stripe_subscription_id="",
            status="checkout_created",
        )
    )
    await db.commit()
    return {"checkout_url": session.url}


@router.get("/me")
async def get_my_subscription(
    current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db_session)
):
    """Return latest subscription status for authenticated user."""
    subscription = await db.scalar(
        select(Subscription).where(Subscription.user_id == current_user.id).order_by(Subscription.id.desc())
    )
    if not subscription:
        return {"subscription": None}
    return {
        "subscription": {
            "status": subscription.status,
            "stripe_customer_id": subscription.stripe_customer_id,
            "stripe_subscription_id": subscription.stripe_subscription_id,
        }
    }


@router.post("/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db_session)):
    """Receive Stripe webhook events and sync subscription status."""
    if not settings.stripe_webhook_secret:
        raise HTTPException(status_code=503, detail="Stripe webhook secret not configured")
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.stripe_webhook_secret)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail="Invalid Stripe signature") from exc

    event_id = event.get("id", "")
    if event_id:
        existing = await db.scalar(select(WebhookEvent).where(WebhookEvent.event_id == event_id))
        if existing:
            return {"received": True, "duplicate": True}
        db.add(WebhookEvent(provider="stripe", event_id=event_id, event_type=event.get("type", "")))

    if event.get("type") == "checkout.session.completed":
        data = event["data"]["object"]
        user_id = data.get("metadata", {}).get("user_id") or data.get("client_reference_id")
        if user_id:
            subscription = await db.scalar(
                select(Subscription).where(Subscription.user_id == int(user_id)).order_by(Subscription.id.desc())
            )
            if subscription:
                subscription.status = "active"
                subscription.stripe_customer_id = data.get("customer", "") or subscription.stripe_customer_id
                subscription.stripe_subscription_id = data.get("subscription", "") or ""
    await db.commit()
    return {"received": True}
