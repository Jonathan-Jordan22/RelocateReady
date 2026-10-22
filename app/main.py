from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import users, locations, scoring, preferences, user_locations

app = FastAPI(title="RelocateReady")

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
