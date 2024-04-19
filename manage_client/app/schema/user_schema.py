from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário")
    username: str | None = Field(default=None)
    password: str

class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

