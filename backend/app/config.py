"""Application configuration via environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings loaded from environment variables / .env file."""

    # App
    APP_NAME: str = "Explore Tourism Brasil Seguro API"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "sqlite:///./tourism.db"

    # Auth
    SECRET_KEY: str = "CHANGE-ME-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    # CORS
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
