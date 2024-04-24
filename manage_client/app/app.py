from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated, Any
from contextlib import asynccontextmanager
from sqlmodel import Session
from database.db import create_db_and_table, engine
from model.user_models import UserAuth, UserCreate, User, UserPublic
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


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)