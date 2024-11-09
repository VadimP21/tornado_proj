import asyncio
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

sync_engine = create_engine(
    os.getenv("DB_URL_POSTGRES_TORNADO_TEST_DB"),
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    os.getenv("DB_URL_POSTGRES_TORNADO_TEST_DB"),
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class BaseProj(DeclarativeBase):
    pass

class Base(DeclarativeBase):
    pass