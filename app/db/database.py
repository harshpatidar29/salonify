from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import settings  # use your custom settings for DB URL

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL  # from .env

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency to get the database session"""
    db = SessionLocal()
    try:
        yield db  # This will provide a database session
    finally:
        db.close()
