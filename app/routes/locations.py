from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.post("/", response_model=schemas.LocationResponse)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Location).filter(models.Location.name == location.name).first()
    if existing:
        return existing
    new_location = models.Location(
        name=location.name,
        country=location.country,
        cost_index=location.cost_index,
        safety_index=location.safety_index
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

@router.get("/", response_model=list[schemas.LocationResponse])
def get_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@router.get("/countries", response_model=list[str])
def get_countries(db: Session = Depends(get_db)):
    countries = db.query(models.Location.country).distinct().all()
    return [c[0] for c in countries]