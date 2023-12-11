from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

@app.on_event('startup')
async def app_startup():
    client_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION
    )

    await init_beanie(
        database=client_db,
        document_models=[
            User,
        ]
    )

