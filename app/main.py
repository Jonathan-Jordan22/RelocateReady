from fastapi import FastAPI
from .database import engine, Base
from .models import User, Preferences, UserLocation, Location  # Import all model classes
from .routes import users, locations, scoring, preferences, user_locations
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
def health_check():
    return {"status": "RelocateReady API is running"}