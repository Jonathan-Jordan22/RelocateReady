from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import User, Preferences, UserLocation, Location  # Import all model classes
from .routes import users, locations, scoring, preferences, user_locations
from . import schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RelocateReady")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(locations.router)
app.include_router(scoring.router)
app.include_router(preferences.router)
app.include_router(user_locations.router)

@app.get("/")

@app.post("/login", response_model=schemas.UserResponse)
def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
def health_check():
    return {"status": "RelocateReady API is running"}