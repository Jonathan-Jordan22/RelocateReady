from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/preferences", tags=["Preferences"])

@router.post("/{user_id}", response_model=schemas.PreferencesResponse)
def create_or_update_preferences(user_id: int, prefs: schemas.PreferencesCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.preferences:
        # Update existing
        for key, value in prefs.dict().items():
            setattr(user.preferences, key, value)
        db.commit()
        db.refresh(user.preferences)
        return user.preferences
    else:
        # Create new
        new_prefs = models.Preferences(user_id=user_id, **prefs.dict())
        db.add(new_prefs)
        db.commit()
        db.refresh(new_prefs)
        return new_prefs
