from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

# Criptografia da senha
def get_password_hash(password: str) -> str:
    return password_context.hash(password)

# Descriptografia da senha
def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

# Create acess_token
def create_acess_token(subject: str | Any, expires_delta: int | None = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    payload = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded

def create_refresh_token(subject: str | Any, expires_delta: int | None = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    payload = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        payload,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded