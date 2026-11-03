from datetime import date

from pydantic import BaseModel


class VisaOptionResponse(BaseModel):
    id: int
    country_id: int
    name: str
    category: str
    summary: str
    eligibility: str
    estimated_cost_usd: int
    processing_time: str | None = None
    official_url: str
    last_verified: date

    class Config:
        from_attributes = True