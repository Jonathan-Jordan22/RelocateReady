from pydantic import BaseModel


class LocationCreate(BaseModel):
    name: str
    country: str
    description: str | None = None
    cost_index: float | None = None
    safety_index: float | None = None
    climate_index: float | None = None
    healthcare_index: float | None = None


class LocationResponse(BaseModel):
    id: int
    name: str
    country: str
    description: str | None = None
    cost_index: float | None = None
    safety_index: float | None = None
    climate_index: float | None = None
    healthcare_index: float | None = None

    class Config:
        from_attributes = True
