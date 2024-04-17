from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_acess_token, create_refresh_token

auth_router = APIRouter()

@auth_router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(
        email = data.username,
        password=data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou Senha estão incorretos"
        )
    
    return {
        "acess_token": create_acess_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }