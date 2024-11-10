from database import session_factory, async_session_factory
from declarative_view_models import WorkersOrm


def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username="Bobby")
        worker_volk = WorkersOrm(username="Volkkk")
        session.add_all([worker_volk, worker_bobr])
        session.commit()


async def insert_data_async():
    async with async_session_factory() as session:
        worker_bobr = WorkersOrm(username="Bobby1")
        worker_volk = WorkersOrm(username="Volkkk1")
        session.add_all([worker_volk, worker_bobr])
        await session.commit()
