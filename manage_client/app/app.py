import uvicorn
from fastapi import FastAPI, HTTPException, status
from datetime import timedelta, timezone, datetime
from sqlmodel import Session, select
from database.db import create_db_and_table, engine
from contextlib import asynccontextmanager
from model.user_models import User, UserRequest, UserResponse, UserAuth
from schema.auth_schema import TokenSchema
from passlib.context import CryptContext
from jose import jwt, JWTError
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_table()
    yield

app = FastAPI()

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user_by_email(email: str):
    with Session(engine) as session:
        statement = select(User).where(User.email == email)
        results = session.exec(statement)
        user = results.one()
        return user

async def authenticated_user(email: str, password: str):
    user: User = await get_user_by_email(email)
    if user is None:
        return False
    if not verify_password(password, user.hash_password):
        return False
    return user

def create_acess_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt




@app.post("/login", summary="Create Acess Token", response_model=TokenSchema)
async def login(form_data: UserAuth):
    user: User = await authenticated_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acess_token_expires = timedelta(days=7)

    acess_token = create_acess_token(
        data={"sub": user.id},
        expires_delta=acess_token_expires
    )
    
    return {
        "acess_token": acess_token,
    }



# Código de Teste(Concluido)
'''
@app.post("/users", tags=["users"])
async def test_user(data: UserRequest):
    user = User(username=data.username, email=data.email, hash_password=get_password_hash(data.password))
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
'''
@app.get("/users", tags=["users"], response_model=list[UserResponse])
async def read_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)