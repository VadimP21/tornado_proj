import asyncio
import os
from typing import Annotated

from dotenv import load_dotenv
from sqlalchemy import create_engine, text, String
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

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_255 = Annotated[str, 255]  # Переиспользование типов на уровне базы данных


class Base(DeclarativeBase):
    # Переиспользование типов на уровне базы данных
    type_annotation_map = {str_255: String(255)}
    pass
