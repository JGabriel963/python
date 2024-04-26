from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .task_model import Task

class UserBase(SQLModel):
    username: str = Field(unique=True)
    email: str = Field(unique=True, index=True)

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: int

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    is_active: bool | None = Field(default=True)

    tasks: list["Task"] = Relationship(back_populates="user")

class UserAuth(SQLModel):
    email: str
    username: str | None = None
    password: str