from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter(prefix="/user-locations", tags=["UserLocations"])

@router.post("/{user_id}/{location_id}")
def save_location(user_id: int, location_id: int, db: Session = Depends(get_db)):
    """
    Save a location to a user's saved locations.
    """
    # Fetch user and location
    user = db.query(models.User).filter(models.User.id == user_id).first()
    location = db.query(models.Location).filter(models.Location.id == location_id).first()

    if not user or not location:
        raise HTTPException(status_code=404, detail="User or location not found")

    # Check if already saved
    existing = db.query(models.UserLocation).filter_by(user_id=user_id, location_id=location_id).first()
    if existing:
        return {"message": "Location already saved"}

    # Save the location
    saved = models.UserLocation(user_id=user_id, location_id=location_id)
    db.add(saved)
    db.commit()
    db.refresh(saved)
    return {"message": f"{location.name} saved for {user.name}"}

@router.get("/{user_id}")
def get_saved_locations(user_id: int, db: Session = Depends(get_db)):
    """
    Get all saved locations for a user.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    saved = db.query(models.UserLocation).filter_by(user_id=user_id).all()
    return [{"location_id": s.location_id, "location_name": s.location.name} for s in saved]
