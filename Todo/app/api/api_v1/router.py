from fastapi import APIRouter
from api.api_v1.handlers import user
from api.auth.jwt import auth_router
from api.api_v1.handlers import tasks

router = APIRouter()

router.include_router(
    user.user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

router.include_router(
    tasks.task_router,
    prefix="/task",
    tags=['task']
)