from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "postgresql://topython_user:lWSZTX4S5EDgY3DAv49Vtb85JmNJgYwK@dpg-clnrb1bj65ls7389vpr0-a.ohio-postgres.render.com/topython"

# DATABASE_URI = "postgresql://jgabriel963:130302jg@localhost/blog"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
