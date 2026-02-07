from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services.scoring import calculate_relocation_score

router = APIRouter(prefix="/score", tags=["Scoring"])


# POST /score/ → score all locations with request weights
@router.post("/", response_model=list[schemas.LocationResponse])
def score_locations(request: schemas.ScoreRequest, db: Session = Depends(get_db)):
    # Get all locations from the database
    locations = db.query(models.Location).all()

    scored_locations = []
    for loc in locations:
        score = calculate_relocation_score(request, loc)
        scored_locations.append((score, loc))
    
    # Sort locations by score descending
    scored_locations.sort(key=lambda x: x[0], reverse=True)

    # Return only the LocationResponse objects
    return [loc for score, loc in scored_locations]


# GET /score/{user_id}/{location_id} → score a single location for a specific user
@router.get("/{user_id}/{location_id}")
def score_location(user_id: int, location_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    if not hasattr(user, "preferences") or user.preferences is None:
        raise HTTPException(status_code=400, detail="User preferences not set")

    score = calculate_relocation_score(user.preferences, location)

    return {
        "user": user.name,
        "location": location.name,
        "score": score
    }