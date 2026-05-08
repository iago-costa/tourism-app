"""Simple token utilities for account recovery."""

import hashlib
import secrets


def generate_reset_token() -> str:
    """Return a random reset token."""
    return secrets.token_urlsafe(32)


def token_digest(token: str) -> str:
    """Return SHA-256 digest for secure persistence."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()
