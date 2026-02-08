from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str


class UserLogin(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True
