from model.user_models import User
from datetime import datetime, timedelta, timezone
from typing import Annotated
from .hash import verify_password
from services.user_service import UserService
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from decouple import config

SECRET_KEY = config('SECRET_KEY')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def authenticate_user(email: str, password: str):
    user: User = await UserService.get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_acess_token(data: dict, expires: timedelta | None = None):
    to_encode = data.copy()
    if expires:
        expire = datetime.now(timezone.utc) + expires
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encode_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await UserService.get_user_by_id(id=int(user_id))
    if user is None:
        raise credentials_exception
    return user