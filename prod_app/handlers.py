from itertools import product

from tornado.web import RequestHandler

from sqlalchemy import insert

from prod_app.models import Product
from prod_app.queries import create_product, get_product_by_name
from prod_app.settings import engine, SessionFactory


class MainHandler(RequestHandler):
    def get(self):
        self.write("Index page")


class CreateProductHandler(RequestHandler):
    def post(self) -> None:
        name = self.get_argument("name")
        try:
            new_product_params = create_product(name)
            self.set_status(201)
            self.write(new_product_params)
        except Exception as exc:
            self.set_status(500)
            self.write({"error": str(exc)})


class GetProductHandler(RequestHandler):
    def get(self, name: str) -> None:
        try:
            current_product_params = get_product_by_name(name)
            self.set_status(201)
            self.write(str(current_product_params))
        except Exception as exc:
            self.set_status(500)
            self.write({"error": str(exc)})
