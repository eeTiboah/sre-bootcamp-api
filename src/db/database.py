
from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.configvars import env_config

SQLALCHEMY_DATABASE_URL = f"postgresql://{env_config.DB_USER}:{env_config.DB_PASSWORD}@localhost:5432/{env_config.DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()