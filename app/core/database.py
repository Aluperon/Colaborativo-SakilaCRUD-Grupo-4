import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()
db_host: str = os.getenv("DB_HOST", "localhost")
db_port: int = int(os.getenv("DB_PORT", 3306))
db_name: str = os.getenv("DB_NAME", "sakila")
db_user: str | None = os.getenv("DB_USER")
db_password: str | None = os.getenv("DB_PASSWORD")

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
