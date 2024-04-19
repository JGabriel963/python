from sqlmodel import SQLModel, create_engine
from decouple import config


# DATABASE_URL = "postgres://python_db_b0nc_user:Utc1YA2V8OZIDLIg7UUPMNGWu6rPTtFW@dpg-cogk34kf7o1s7380uiu0-a.oregon-postgres.render.com/python_db_b0nc"

DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)