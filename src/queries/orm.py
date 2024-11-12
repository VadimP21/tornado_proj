from sqlalchemy import select, func, cast, Integer, and_
from sqlalchemy.dialects.mysql import insert

from database import session_factory, async_session_factory, sync_engine, Base, str_255
from models import WorkersOrm, Workload, ResumesOrm


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
    def select_workers():
        with session_factory() as session:
            # конкретный объект через id
            # worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            # несколько объектов аналогично select из core
            query = select(WorkersOrm)
            result = session.execute(query)
            # workers = result.all()  # вывод списка кортежей [(model.WorkerORM object...), (model.WorkerORM object...)]
            workers = (
                result.scalars().all()
            )  # вывод списка моделей [model.WorkerORM object..., model.WorkerORM object...]
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 1, new_username: str_255 = "Misha"):
        with session_factory() as session:
            worker_michel = session.get(WorkersOrm, worker_id)
            worker_michel.username = new_username
            session.expire_all()  # отменяет изменения
            session.refresh()  # обновляет до значений БД в данный момент времени
            session.commit()

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_mitchel = WorkersOrm(username="Mitchel")
            session.add_all([worker_mitchel, worker_jack])
            # session.flush()  # отправляет изменения в БД, присваивает id объектам для дальнейшей работы с ними до commit

            session.commit()

    @staticmethod
    def insert_resumes():
        with session_factory() as session:
            resume_jack_1 = ResumesOrm(
                title="Python Junior Developer",
                compensation=50000,
                workload=Workload.fulltime,
                worker_id=1,
            )
            resume_jack_2 = ResumesOrm(
                title="Python Разработчик",
                compensation=150000,
                workload=Workload.fulltime,
                worker_id=1,
            )
            resume_mike_1 = ResumesOrm(
                title="Python Data Engineer",
                compensation=250000,
                workload=Workload.parttime,
                worker_id=2,
            )
            resume_mike_2 = ResumesOrm(
                title="Data Scientist",
                compensation=300000,
                workload=Workload.fulltime,
                worker_id=2,
            )
            session.add_all(
                [resume_jack_1, resume_jack_2, resume_mike_2, resume_mike_1]
            )
            session.commit()

    @staticmethod
    def insert_additional_resumes():
        with session_factory() as session:
            workers = [
                {"username": "Artem"},
                {"username": "Roman"},
                {"username": "Petr"},
            ]
            resumes = [
                {
                    "title": "Python Разработчик",
                    "compensation": 60000,
                    "workload": "fulltime",
                    "worker_id": 3,
                },
                {
                    "title": "Machine learning engineer",
                    "compensation": 70000,
                    "workload": "parttime",
                    "worker_id": 3,
                },
                {
                    "title": "Python Data Scientist",
                    "compensation": 80000,
                    "workload": "parttime",
                    "worker_id": 4,
                },
                {
                    "title": "Python Analyst",
                    "compensation": 90000,
                    "workload": "fulltime",
                    "worker_id": 4,
                },
                {
                    "title": "Python Junior Developer",
                    "compensation": 100000,
                    "workload": "fulltime",
                    "worker_id": 5,
                },
            ]
            insert_workers = insert(WorkersOrm).values(workers)
            insert_resumes = insert(ResumesOrm).values(resumes)
            session.execute(insert_workers)
            session.execute(insert_resumes)
            session.commit()

    @staticmethod
    def select_resumes_avg_compensation(like_language: str = "Python"):
        with session_factory() as session:
            """
            select workload, avg(compensation)::int as ag_compensation
            from resumes
            where title like '%Python%" and compensation > 40000
            group by workload

            SELECT resumes.workload, CAST(avg(resumes.compensation) AS INTEGER) AS avg_compensation
            FROM resumes
            WHERE (resumes.title LIKE '%' || 'Python' || '%') AND resumes.compensation > 40000 GROUP BY resumes.workload
            HAVING CAST(avg(resumes.compensation) AS INTEGER) > 70000
            """
            query = (
                select(
                    ResumesOrm.workload,
                    cast(func.avg(ResumesOrm.compensation), Integer).label(
                        "avg_compensation"
                    ),
                )
                .select_from(ResumesOrm)
                .filter(
                    and_(
                        ResumesOrm.title.contains(like_language),
                        ResumesOrm.compensation > 40000,
                    )
                )
                .group_by(ResumesOrm.workload)
                .having(cast(func.avg(ResumesOrm.compensation), Integer) > 70000)
            )
            print(query.compile(compile_kwargs={"literal_binds": True}))
            res = session.execute(query)
            result = res.all()
            print(result[0].workload, result[1].avg_compensation)
