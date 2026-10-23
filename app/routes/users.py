from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from app.models.user import User
from ..dependencies import get_db, get_current_user
from ..utils.password import hash_password, verify_password
from ..auth import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.Token)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password_hash=hash_password(user.password),
    )
    db.add(new_user)
    db.flush()  # assigns new_user.id without committing yet

    db.add(models.Preferences(user_id=new_user.id))
    db.commit()  # user + preferences saved together, or not at all

    return {
        "access_token": create_access_token(new_user.id),
        "token_type": "bearer",
        "user": schemas.UserResponse.model_validate(new_user),
    }

@router.get("/me", response_model=schemas.UserResponse)
def read_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.post("/login", response_model=schemas.Token)
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Verify the password
    if not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {
        "access_token": create_access_token(user.id),
        "token_type": "Bearer",
        "user": schemas.UserResponse.model_validate(user),
    }

@router.patch("/me", response_model=schemas.UserResponse)
@router.put("/me", response_model=schemas.UserResponse)
def update_me(
    user_update: schemas.UserUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user_update.email and user_update.email != current_user.email:
        existing_email = db.query(models.User).filter(models.User.email == user_update.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        current_user.email = user_update.email

    if user_update.first_name is not None:
        current_user.first_name = user_update.first_name
    if user_update.last_name is not None:
        current_user.last_name = user_update.last_name

    db.commit()
    db.refresh(current_user)
    return current_user

@router.delete("/me")
def delete_me(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db.query(models.Preferences).filter(models.Preferences.user_id == current_user.id).delete()
    db.query(models.UserLocation).filter(models.UserLocation.user_id == current_user.id).delete()
    db.delete(current_user)
    db.commit()
    return {"message": "Account deleted successfully"}