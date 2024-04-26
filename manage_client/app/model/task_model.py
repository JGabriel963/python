from sqlmodel import SQLModel, Field, Relationship
from .user_models import User
from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .user_models import User

class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: str

class TaskCreate(TaskBase):
    pass

class TaskPublic(TaskBase):
    id: int
    status: bool
    user_id: int

class TaskUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    status: bool | None = None

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    status: bool | None = Field(default=False)

    created_at: datetime | None = Field(default=datetime.now())
    updated_at: datetime | None = Field(default=datetime.now())
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="tasks")