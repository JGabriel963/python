from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated, Any
from contextlib import asynccontextmanager
from sqlmodel import Session, select
from database.db import create_db_and_table, engine
from model.user_models import UserAuth, UserCreate, User, UserPublic
from model.task_model import TaskCreate, Task, TaskPublic, TaskUpdate
from utils.hash import get_password_hash
from utils.auth import authenticate_user, create_acess_token, get_current_user
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_table()
    yield

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(lifespan=lifespan)

# User Routes
@app.post("/login")
async def login(user: UserAuth):
    user: User = await authenticate_user(email=user.email, password=user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorret username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    acess_token = create_acess_token(data={"sub": str(user.id), "email": user.email})
    return {
        "acess_token": acess_token
    }
     
@app.post("/signup", response_model=UserPublic)
async def signup(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = get_password_hash(user.password)
    db_user = User.model_validate(user, update={"hashed_password": hashed_password})
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/me", response_model=UserPublic)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

# Task Routes
@app.get("/tasks", response_model=list[TaskPublic])
async def get_tasks(current_user: Annotated[User, Depends(get_current_user)], session: Session = Depends(get_session)):
    statement = select(Task).where(Task.user_id == current_user.id)
    tasks = session.exec(statement).all()
    return tasks
    

@app.post("/tasks", response_model=TaskPublic)
async def create_task(task: TaskCreate, current_user: Annotated[User, Depends(get_current_user)], session: Session = Depends(get_session)):
    task = Task(title=task.title, description=task.description, user=current_user)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.get("/tasks/{task_id}", response_model=TaskPublic)
async def get_one_task(task_id: int, current_user: Annotated[User, Depends(get_current_user)], session: Session = Depends(get_session)):
    statement = select(Task).where(Task.user_id == current_user.id).where(Task.id == task_id)
    task = session.exec(statement).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task is not found"
        )
    return task

@app.put("/tasks/{task_id}", response_model=TaskPublic)
async def update_task(task_id: int, task: TaskUpdate, current_user: Annotated[User, Depends(get_current_user)], session: Session = Depends(get_session)):
    statement = select(Task).where(Task.user_id == current_user.id).where(Task.id == task_id)
    db_task = session.exec(statement).one()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data = task.model_dump(exclude_unset=True)
    db_task.sqlmodel_update(task_data)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: Annotated[User, Depends(get_current_user)], session: Session = Depends(get_session)):
    pass


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)