from sqlmodel import SQLModel, Field, Relationship
from .user_models import User

class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: str

class TaskCreate(TaskBase):
    pass

class TaskPublic(TaskBase):
    id: int
    status: bool

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    status: bool | None = Field(default=False)

    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="tasks")