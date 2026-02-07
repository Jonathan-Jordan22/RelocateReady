from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import users, locations, score

app = FastAPI(title="RelocateReady")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(locations.router)
app.include_router(score.router)

@app.get("/")
def health_check():
    return {"status": "RelocateReady API is running"}