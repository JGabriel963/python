from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User
from models.task_model import Task
from api.api_v1.router import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def app_init(app: FastAPI):
    client_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    ).todoapp

    await init_beanie(
        database=client_db,
        document_models=[
            User,
            Task
        ]
    )
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=app_init
)

app.include_router(
    router,
    prefix=settings.API_V1_STR
)