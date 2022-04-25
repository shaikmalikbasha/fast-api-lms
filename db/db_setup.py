from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/fast_api_lms"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/fast_api_lms"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


# DB Utility
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Async DB Utility
async def get_db_sync():
    # with
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
