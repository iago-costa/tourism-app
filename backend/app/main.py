from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine
from app.middleware.production_guards import validate_production_secret
from app.middleware.rate_limit_auth import AuthRateLimitMiddleware
from app.middleware.security_headers import (
    SecurityHeadersMiddleware,
    fastapi_openapi_urls,
    is_production_env,
)
from app.models import Base
from app.routes import attractions, auth, billing, health, reviews

_is_prod = is_production_env(settings.environment)

app = FastAPI(
    title=settings.app_name,
    description="Backend API for tourism.vivdio.com.",
    version="0.1.0",
    **fastapi_openapi_urls(is_production=_is_prod),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeadersMiddleware, hsts=_is_prod)
app.add_middleware(AuthRateLimitMiddleware, enabled=_is_prod)

app.include_router(health.router, tags=["Health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(billing.router, prefix="/api/v1/billing", tags=["Billing"])
app.include_router(attractions.router, prefix="/api/v1/attractions", tags=["Attractions"])
app.include_router(reviews.router, prefix="/api/v1/reviews", tags=["Reviews"])


@app.on_event("startup")
async def startup() -> None:
    validate_production_secret(
        "JWT_SECRET_KEY", settings.jwt_secret_key, is_production=_is_prod
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
