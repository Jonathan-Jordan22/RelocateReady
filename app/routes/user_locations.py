from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_current_user, get_db

router = APIRouter(prefix="/user-locations", tags=["UserLocations"])


@router.get("/me", response_model=list[schemas.LocationResponse])
def get_my_saved_locations(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    saved = db.query(models.UserLocation).filter_by(user_id=current_user.id).all()
    return [s.location for s in saved]


@router.post("/me/{location_id}")
def save_location(
    location_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    location = db.get(models.Location, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    existing = db.query(models.UserLocation).filter_by(
        user_id=current_user.id, location_id=location_id
    ).first()
    if existing:
        return {"message": "Location already saved"}

    db.add(models.UserLocation(user_id=current_user.id, location_id=location_id))
    db.commit()
    return {"message": f"{location.name} saved"}


@router.delete("/me/{location_id}")
def remove_location(
    location_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    saved = db.query(models.UserLocation).filter_by(
        user_id=current_user.id, location_id=location_id
    ).first()
    if not saved:
        raise HTTPException(status_code=404, detail="Saved location not found")

    db.delete(saved)
    db.commit()
    return {"message": "Location removed from saved list"}