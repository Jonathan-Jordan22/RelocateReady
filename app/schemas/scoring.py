from pydantic import BaseModel


class ScoreRequest(BaseModel):
    cost_index_weight: float = 0.5
    safety_index_weight: float = 0.5
    climate_importance: float = 0.0
    healthcare_importance: float = 0.0
