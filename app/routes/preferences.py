from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_current_user, get_db

router = APIRouter(prefix="/preferences", tags=["Preferences"])


@router.get("/me", response_model=schemas.PreferencesResponse)
def get_my_preferences(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    prefs = db.query(models.Preferences).filter(models.Preferences.user_id == current_user.id).first()
    if not prefs:
        raise HTTPException(status_code=404, detail="Preferences not found")
    return prefs


@router.post("/me", response_model=schemas.PreferencesResponse)
def save_my_preferences(
    prefs: schemas.PreferencesCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_prefs = db.query(models.Preferences).filter(models.Preferences.user_id == current_user.id).first()
    if not user_prefs:
        user_prefs = models.Preferences(user_id=current_user.id, **prefs.model_dump())
        db.add(user_prefs)
    else:
        for key, value in prefs.model_dump().items():
            setattr(user_prefs, key, value)
    db.commit()
    db.refresh(user_prefs)
    return user_prefs