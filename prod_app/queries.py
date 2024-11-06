from sqlalchemy.orm import sessionmaker
from tornado import gen
from prod_app.settings import engine
from prod_app.models import Product

SessionFactory = sessionmaker(bind=engine)


@gen.coroutine
def query_product_by_name(name):
    session = SessionFactory()

    try:
        result = session.query(Product).filter(Product.name == name).first()
        raise gen.Return(result)
    finally:
        session.close()


def query_add_product_by_name(name):
    session = SessionFactory()
    prod = Product(name=name)
    session.add(prod)
    session.close()
