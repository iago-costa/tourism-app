"""
Explore Tourism Brasil Seguro — Backend API
=============================================
FastAPI-based REST API for the tourism app.

Provides endpoints for:
- Tourist attractions (CRUD, search, filtering)
- User authentication & profiles
- Reviews and ratings
- Itinerary management
- Emergency contacts by region
- Partner/service listings
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import attractions, auth, health, reviews

app = FastAPI(
    title="Explore Tourism Brasil Seguro API",
    description="Backend API for the tourism app — safe, multilingual tourism in Brazil.",
    version="0.1.0",
)

# CORS — allow the React Native app to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health.router, tags=["Health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(attractions.router, prefix="/api/v1/attractions", tags=["Attractions"])
app.include_router(reviews.router, prefix="/api/v1/reviews", tags=["Reviews"])
