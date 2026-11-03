from pydantic import BaseModel
from datetime import date


class LocationCreate(BaseModel):
    name: str
    country: str
    country_id: int
    description: str | None = None
    cost_index: float | None = None
    safety_index: float | None = None
    climate_index: float | None = None
    healthcare_index: float | None = None
    avg_rent_usd: int | None = None
    monthly_living_cost_usd: int | None = None
    cost_data_as_of: date | None = None


class LocationResponse(BaseModel):
    id: int
    name: str
    country: str
    country_id: int
    description: str | None = None
    cost_index: float | None = None
    safety_index: float | None = None
    climate_index: float | None = None
    healthcare_index: float | None = None
    avg_rent_usd: int | None = None
    monthly_living_cost_usd: int | None = None
    cost_data_as_of: date | None = None

    class Config:
        from_attributes = True
