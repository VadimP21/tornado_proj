from sqlalchemy import select

from database import session_factory, async_session_factory, sync_engine, Base, str_255
from models import WorkersOrm


class AsyncOrm:
    @staticmethod
    async def insert_data_async():
        async with async_session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_mitchel = WorkersOrm(username="Mitchel")
            session.add_all([worker_mitchel, worker_jack])
            await session.commit()


class SyncORM:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_mitchel = WorkersOrm(username="Mitchel")
            session.add_all([worker_mitchel, worker_jack])
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            # конкретный объект через id
            # worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            # несколько объектов аналогично select из core
            query = select(WorkersOrm)
            result = session.execute(query)
            # workers = result.all()  # вывод списка кортежей [(model.WorkerORM object...), (model.WorkerORM object...)]
            workers = result.scalars().all()  # вывод списка моделей [model.WorkerORM object..., model.WorkerORM object...]
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 1, new_username: str_255 = "Misha"):
        with session_factory() as session:
            worker_michel = session.get(WorkersOrm, worker_id)
            worker_michel.username = new_username
            session.commit()