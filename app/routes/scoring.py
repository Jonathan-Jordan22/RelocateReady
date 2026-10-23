from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db, get_current_user
from ..services.scoring import calculate_relocation_score
from ..services.ai_predict import predict_best_locations

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


#@router.get("/me/{location_id}")
def score_location(
    location_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    location = db.get(models.Location, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    if current_user.preferences is None:
        raise HTTPException(status_code=400, detail="User preferences not set")

    return {
        "location": location.name,
        "score": calculate_relocation_score(current_user.preferences, location),
    }


@router.post("/me/ranked")
def ranked_locations(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get the current user's saved locations, ranked by relocation score."""
    if current_user.preferences is None:
        db.add(models.Preferences(user_id=current_user.id))
        db.commit()
        db.refresh(current_user)

    saved = db.query(models.UserLocation).filter_by(user_id=current_user.id).all()
    if not saved:
        return {"message": "No saved locations"}

    scored = [
        (calculate_relocation_score(current_user.preferences, s.location), s.location)
        for s in saved
    ]
    scored.sort(key=lambda x: x[0], reverse=True)

    return [
        {"score": score, "location": schemas.LocationResponse.model_validate(loc)}
        for score, loc in scored
    ]


@router.get("/me/ai-suggest")
def ai_suggest(
    top_n: int = 3,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return the top predicted relocation locations for the current user."""
    if current_user.preferences is None:
        raise HTTPException(status_code=404, detail="Preferences not found")

    locations = db.query(models.Location).all()
    return {"top_locations": predict_best_locations(current_user, locations, top_n)}