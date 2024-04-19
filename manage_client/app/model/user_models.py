from sqlmodel import Field, SQLModel, create_engine
from pydantic import BaseModel, EmailStr

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

class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    hash_password: str
    is_active: bool | None = Field(default=True)

