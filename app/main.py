from fastapi import FastAPI
from .database import engine, Base
from .models import User, UserPreferences, UserLocation, Location  # Import all model classes
from .routes import users, locations, scoring

app = FastAPI(title="RelocateReady")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(locations.router)
app.include_router(scoring.router)

@app.get("/")
def health_check():
    return {"status": "RelocateReady API is running"}