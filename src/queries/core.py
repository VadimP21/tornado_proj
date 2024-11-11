from multiprocessing.pool import worker

from sqlalchemy import select, text, update
from sqlalchemy.dialects.mysql import insert

from models import WorkersOrm
from src.database import sync_engine, Base, async_engine, str_255


class AsyncCore:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


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

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(WorkersOrm)
            result = conn.execute(query)
            # workers = result.scalars().all() #  вывод списка id
            workers = result.all()  # вывод списка кортежей (id, username)
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str_255 = "Misha"):
        with sync_engine.connect() as conn:
            # stmt = text("UPDATE workers SET username=:username WHERE id=:id").bindparams(
            #     username=new_username,
            #     id=worker_id)  # с целью защиты от SQLInjection передача параметра new_username(пользовательский ввод) в username(столбец БД), id соответственно

            stmt = (
                update(WorkersOrm).values(username=new_username)
                # .where(WorkersOrm.id==worker_id) #  аналогично .filter_by(id=worker_id)
                .filter_by(id=worker_id)
            )

            conn.execute(stmt)
            conn.commit()
