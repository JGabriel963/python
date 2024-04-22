from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import Field, Session, SQLModel, create_engine, select

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class HeroCreate(HeroBase):
    pass

class HeroPublic(HeroBase):
    id: int

sqlite_url = "sqlite:///database.db"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/heroes", response_model=HeroPublic)
async def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        db_hero = Hero.model_validate(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero

@app.get("/heroes", response_model=list[HeroPublic])
async def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes

@app.get("/heroes/{hero_id}", response_model=HeroPublic)
async def read_hero(hero_id: int, name: str | None = None):
    if name:
        with Session(engine) as session:
            statement = select(Hero).where(Hero.name == name)
            results = session.exec(statement)
            hero = results.first()
            return hero
    with Session(engine) as session:
        hero = session.get(Hero, hero_id)
        if not Hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero