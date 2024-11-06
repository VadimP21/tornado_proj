from tornado.web import RequestHandler

from prod_app.queries import query_product_by_name, query_add_product_by_name


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")


class ProductHandler(RequestHandler):
    async def get(self, name):
        prod = await query_product_by_name(name)
        if prod:
            self.write(f"Product found: {prod.name}")
        else:
            self.write("Product not found")


class AddProductHandler(RequestHandler):
    def post(self, name):
        pass
