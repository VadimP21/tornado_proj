from itertools import product

from tornado.web import RequestHandler

from sqlalchemy import insert

from prod_app.models import Product
from prod_app.settings import engine, SessionFactory


class MainHandler(RequestHandler):
    def get(self):
        self.write("Index page")


def create_product(name):
    with SessionFactory() as session:
        new_product = Product(name=name)  # Создаем объект продукта
        session.add(new_product)  # Добавляем объект в сессию
        session.commit()  # Сохраняем изменения в БД
        product_params = {
            "id": new_product.id,
            "name": new_product.name,
            "category": new_product.category,
        }
        return product_params  # Возвращаем объект продукта
    # stmt = insert(Product).values(name=name)
    # with engine.connect() as conn:
    #     result = conn.execute(stmt)
    #     conn.commit()
    #     product_id = result.inserted_primary_key[0]
    #     # print(result.keys())
    #     return product_id


class CreateProductHandler(RequestHandler):
    def post(self):
        name = self.get_argument("name")
        try:
            product_params = create_product(name)
            self.set_status(201)
            self.write(product_params)
        except Exception as exc:
            self.set_status(500)
            self.write({"error": str(exc)})


class GetProductHandler(RequestHandler):
    pass
