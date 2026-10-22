import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./relocateready.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("swlite") else []

engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()