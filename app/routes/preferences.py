from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/preferences", tags=["Preferences"])

@router.get("/{user_id}", response_model=schemas.ScoreRequest)
def get_preferences(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Preferences).filter(models.Preferences.user_id == user_id).first()
    if not user:
        # Return default preferences if none exist
        return {"cost_index_weight": 0.5, "safety_index_weight": 0.5}
    return user

@router.post("/{user_id}", response_model=schemas.ScoreRequest)
def create_or_update_preferences(user_id: int, prefs: schemas.ScoreRequest, db: Session = Depends(get_db)):
    user_prefs = db.query(models.Preferences).filter(models.Preferences.user_id == user_id).first()
    if not user_prefs:
        user_prefs = models.Preferences(user_id=user_id, **prefs.dict())
        db.add(user_prefs)
    else:
        for key, value in prefs.dict().items():
            setattr(user_prefs, key, value)
    db.commit()
    db.refresh(user_prefs)
    return user_prefs