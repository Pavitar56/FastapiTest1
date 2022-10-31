from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote 

#SQLALCHAMY_DATABASE_URL=

#SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine("mysql+mysqlconnector://root:%s@localhost:3306/finaldb" % quote('Pavi@_8156'))

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
