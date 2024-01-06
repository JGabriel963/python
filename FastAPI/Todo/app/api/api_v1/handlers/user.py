from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth
from services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post('/add', summary='Adiciona Usuário')
async def add_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username ou e-mail deste usuário já existe'
        )