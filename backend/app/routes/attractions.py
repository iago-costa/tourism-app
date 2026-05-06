"""Tourist attractions routes — search, list, detail."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_attractions():
    """List all tourist attractions with optional filtering."""
    return {
        "message": "Attractions list — TODO: implement",
        "data": [],
    }


@router.get("/{attraction_id}")
async def get_attraction(attraction_id: int):
    """Get details for a specific tourist attraction."""
    return {
        "message": f"Attraction {attraction_id} detail — TODO: implement",
    }


@router.get("/search")
async def search_attractions(q: str = ""):
    """Search attractions by name, category, or location."""
    return {
        "message": f"Search results for '{q}' — TODO: implement",
        "data": [],
    }
