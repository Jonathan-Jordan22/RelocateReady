from pydantic import BaseModel

class PreferencesCreate(BaseModel):
    cost_importance: float = 0.5
    safety_importance: float = 0.5
    climate_importance: float = 0.0
    healthcare_importance: float = 0.0

class PreferencesResponse(PreferencesCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
