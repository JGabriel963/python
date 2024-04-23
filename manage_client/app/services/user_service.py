from typing import Optional
from sqlmodel import Session, select
from database.db import engine
from model.user_models import User


class UserService:
    @staticmethod
    async def get_user_by_email(email: str):
        with Session(engine) as session:
            statement = select(User).where(User.email == email)
            result = session.exec(statement)
            user = result.first()
            return user
    
    @staticmethod
    async def get_user_by_id(id: int):
        with Session(engine) as session:
            user = session.get(User, id)
            return user