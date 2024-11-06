import asyncio

import tornado.ioloop
import tornado.web

from handlers import MainHandler, GetProductHandler, CreateProductHandler
from prod_app.models import Base
from prod_app.settings import engine


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/product/([^/]+)", GetProductHandler),
            (r"/product", CreateProductHandler),
        ]
    )


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
