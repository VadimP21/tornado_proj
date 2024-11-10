from sqlalchemy.dialects.mysql import insert

from models import WorkersOrm
from src.database import sync_engine, Base, async_engine


class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            # Сырой запрос
            # stmt = """INSERT INTO users (username) VALUES
            # ('Jack'),
            # ('Mitchel');
            # """
            # Query builder
            stmt = insert(WorkersOrm).values(
                [
                    {"username": "Jack"},
                    {"username": "Mitchel"},
                ]
            )
            conn.execute(stmt)
            conn.commit()


class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
