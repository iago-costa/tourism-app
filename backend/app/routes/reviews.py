"""Reviews and ratings routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/attraction/{attraction_id}")
async def list_reviews(attraction_id: int):
    """List reviews for a specific attraction."""
    return {
        "message": f"Reviews for attraction {attraction_id} — TODO: implement",
        "data": [],
    }


@router.post("/attraction/{attraction_id}")
async def create_review(attraction_id: int):
    """Submit a new review for an attraction."""
    return {
        "message": f"Create review for attraction {attraction_id} — TODO: implement",
    }
