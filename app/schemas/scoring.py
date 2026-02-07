from pydantic import BaseModel


class ScoreRequest(BaseModel):
    cost_index_weight: float = 0.5
    safety_index_weight: float = 0.5
