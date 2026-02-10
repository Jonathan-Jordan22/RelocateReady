from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import User, Preferences, UserLocation, Location  # Import all model classes
from .routes import users, locations, scoring, preferences, user_locations
from . import schemas
from .utils.password import verify_password
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RelocateReady")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://relocate-ready.vercel.app"],
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
def health_check():
    return {"status": "RelocateReady API is running"}

@app.post("/login", response_model=schemas.UserResponse)
def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Verify the password
    if not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return user
    return {"status": "RelocateReady API is running"}