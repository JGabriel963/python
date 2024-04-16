from typing import Any
from enum import Enum
from passlib.context import CryptContext
from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Tags(Enum):
    items = "items"
    users = "users"

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def password_hasher(raw_password: str):
    return pwd_context.hash(raw_password)

def fake_save_user(user_in: UserIn):
    hashed_password = password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user", response_model=UserOut, status_code=status.HTTP_201_CREATED, tags=[Tags.users])
async def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved