"""Application settings for Tourism backend."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings loaded from environment."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Tourism API"
    app_env: str = "development"
    app_debug: bool = False

    database_url: str = "postgresql+asyncpg://tourism:tourism_dev@localhost:5432/tourism_dev"

    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    jwt_secret_key: str = "change-this-secret"
    jwt_algorithm: str = "HS256"

    google_oauth_client_id: str = ""
    google_oauth_client_secret: str = ""
    google_oauth_redirect_uri: str = "https://tourism.vivdio.com/auth/google/callback"
    google_oauth_authorize_url: str = "https://accounts.google.com/o/oauth2/v2/auth"

    stripe_secret_key: str = ""
    stripe_price_monthly_id: str = ""
    stripe_success_url: str = "https://tourism.vivdio.com/billing/success"
    stripe_cancel_url: str = "https://tourism.vivdio.com/billing/cancel"
    stripe_webhook_secret: str = ""

    resend_api_key: str = ""
    resend_from_email: str = "accounts@tourism.vivdio.com"
    frontend_url: str = "https://tourism.vivdio.com"


settings = Settings()
