from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True

class LocationCreate(BaseModel):
    name: str
    country: str
    cost_index: float = None
    safety_index: float = None

class LocationResponse(BaseModel):
    id: int
    name: str
    country: str
    cost_index: float = None
    safety_index: float = None

    class Config:
        from_attributes = True

class ScoreRequest(BaseModel):
    cost_index_weight: float = 0.5
    safety_index_weight: float = 0.5