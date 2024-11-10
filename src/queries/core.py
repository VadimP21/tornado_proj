from sqlalchemy import text
from sqlalchemy.dialects.mysql import insert

# from declarative_view_models import Base
from src.imperative_view_models import users_table
from src.database import sync_engine, async_engine
from src.imperative_view_models import metadata_obj


# FROM LEGACY FILE queries.py
# from src.declarative_view_models import Product
# from src.database import SessionFactory
# from sqlalchemy import select
#
#
# def create_product(name: str) -> dict:
#     with SessionFactory() as session:
#         new_product = Product(name=name)
#         session.add(new_product)
#         session.commit()
#         new_product_params = {
#             "id": new_product.id,
#             "name": new_product.name,
#             "category": new_product.category,
#         }
#         return new_product_params
#
#
# def get_product_by_name(name: str):
#     with SessionFactory() as session:
#         stmt = select(Product).where(Product.name == name)
#         current_products = session.scalars(stmt).all()
#         result = []
#         if not current_products:
#             return {}
#         for prod in current_products:
#             prod_params = {
#                 "id": prod.id,
#                 "name": prod.name,
#                 "category": prod.category,
#             }
#             result.append(prod_params)
#         return result


async def get_123():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT VERSION()"))


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # Сырой запрос
        # stmt = """INSERT INTO users (username) VALUES
        # ('BOBR'),
        # ('Volk');
        # """
        # Query builder
        stmt = insert(users_table).values(
            [
                {"username": "Bob"},
                {"username": "Rex"},
            ]
        )
        conn.execute(stmt)
        conn.commit()
