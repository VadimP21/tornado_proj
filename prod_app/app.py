import tornado.ioloop
import tornado.web

from handlers import MainHandler, ProductHandler, AddProductHandler


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/product/add/([^/]+)", AddProductHandler),
            (r"/product/([^/]+)", ProductHandler),
        ]
    )


if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
