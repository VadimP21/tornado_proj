import asyncio
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

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

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
