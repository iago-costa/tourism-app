"""Production startup checks and minimal public auth config."""

from __future__ import annotations

_INSECURE_SECRETS = frozenset(
    {
        "change-me-in-production-use-random-64-char-string",
        "change-me-in-production",
        "change-me-to-a-random-64-char-string",
        "change-this-secret",
        "dev-secret-change-in-production",
        "content-secret-key",
        "leiloes-secret",
        "test-secret-key",
        "test-secret-key-ci",
        "test-secret",
    }
)


def is_insecure_secret(value: str, *, min_length: int = 32) -> bool:
    normalized = value.strip()
    if len(normalized) < min_length:
        return True
    lowered = normalized.lower()
    if lowered in _INSECURE_SECRETS:
        return True
    if lowered.startswith("change-") or lowered.startswith("dev-"):
        return True
    return False


def validate_production_secret(name: str, value: str, *, is_production: bool) -> None:
    """Fail fast when a default/weak secret would run in production."""
    if not is_production:
        return
    if is_insecure_secret(value):
        raise RuntimeError(f"{name} must be set to a strong value in production")


def build_auth_config_response(
    *,
    is_production: bool,
    allow_password_auth: bool,
    google_oauth_configured: bool,
    social_oauth_per_user: bool = False,
) -> dict[str, bool]:
    """Production exposes only password capability; dev exposes full UI flags."""
    if is_production:
        return {"allow_password_auth": allow_password_auth}
    return {
        "allow_password_auth": allow_password_auth,
        "google_oauth_configured": google_oauth_configured,
        "social_oauth_per_user": social_oauth_per_user,
    }
