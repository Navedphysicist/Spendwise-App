# Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create Engine => Database

DATABASE_URL = 'sqlite:///./spendwise_app.db'

engine  = create_engine(DATABASE_URL,connect_args={'check_same_thread':False})

# Session =>  Python + Sqlite queries => Database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base => To connect models
Base = declarative_base()

#Generator Function => Return session when called
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
