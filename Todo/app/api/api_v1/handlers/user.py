from fastapi import APIRouter, HTTPException, status
import pymongo.errors
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post("/adicionar", summary="Adicionar Usuário", response_model=UserDetail)
async def adicionar_usuario(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_4007,
            detail="Username ou e-mail deste usuário já existe"
        )