from pydantic import BaseModel, EmailStr, field_validator
import re


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str | None = None
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str | None = None

    class Config:
        from_attributes = True
