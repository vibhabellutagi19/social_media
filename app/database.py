from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Settings

app_settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{app_settings.db_username}:{app_settings.db_password}@{app_settings.db_host}/{app_settings.db_name}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# to talk to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# to create a model, we need to extend the Base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
