from database import session_factory, async_session_factory, sync_engine, Base
from models import WorkersOrm


class SyncORM:

    @staticmethod
    def create_tables():
        # sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        # sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_mitchel = WorkersOrm(username="Mitchel")
            session.add_all([worker_mitchel, worker_jack])
            session.commit()


class AsyncOrm:
    @staticmethod
    async def insert_data_async():
        async with async_session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_mitchel = WorkersOrm(username="Mitchel")
            session.add_all([worker_mitchel, worker_jack])
            await session.commit()
