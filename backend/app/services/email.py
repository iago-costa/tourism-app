"""Resend email service helpers."""

import httpx

from app.config import settings


async def send_password_reset_email(email: str, token: str) -> None:
    """Send password reset email through Resend API."""
    if not settings.resend_api_key:
        return

    reset_url = f"{settings.frontend_url}/recover-account?token={token}"
    payload = {
        "from": settings.resend_from_email,
        "to": [email],
        "subject": "Recuperacao de conta Tourism",
        "html": (
            "<p>Recebemos um pedido de recuperacao de conta.</p>"
            f"<p><a href='{reset_url}'>Clique aqui para redefinir a senha</a></p>"
        ),
    }
    headers = {"Authorization": f"Bearer {settings.resend_api_key}"}
    async with httpx.AsyncClient(timeout=20) as client:
        await client.post("https://api.resend.com/emails", json=payload, headers=headers)
