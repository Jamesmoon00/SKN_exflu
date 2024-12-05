from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class UserResponse(BaseModel):
    email: str
    name: str
