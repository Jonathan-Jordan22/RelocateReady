from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/score", tags=["Score"])

@router.post("/", response_model=list[schemas.LocationResponse])
def score_locations(request: schemas.ScoreRequest, db: Session = Depends(get_db)):
    locations = db.query(models.Location).all()

    scored_locations = []
    for loc in locations:
        score = 0 
        if loc.cost_index is not None:
            score+= (100 - loc.cost_index) * request.cost_index_weight
        if loc.safety_index is not None:
            score+= loc.safety_index * request.safety_index_weight
        scored_locations.append((score, loc))
    
    scored_locations.sort(key=lambda x: x[0], reverse=True)

    return [loc for score, loc in scored_locations]
