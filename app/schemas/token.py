from pydantic import BaseModel

from .user import UserResponse


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    user: UserResponse