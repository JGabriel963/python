from sqlmodel import SQLModel, create_engine

# DATABASE_URL="postgresql://JGabriel963:Gd3bkE8fyXzc@ep-dawn-cherry-a5ibq6th.us-east-2.aws.neon.tech/my_db?sslmode=require"

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)