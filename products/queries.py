from models import Product
from database import SessionFactory
from sqlalchemy import select


def create_product(name: str) -> dict:
    with SessionFactory() as session:
        new_product = Product(name=name)
        session.add(new_product)
        session.commit()
        new_product_params = {
            "id": new_product.id,
            "name": new_product.name,
            "category": new_product.category,
        }
        return new_product_params


def get_product_by_name(name: str):
    with SessionFactory() as session:
        stmt = select(Product).where(Product.name == name)
        current_products = session.scalars(stmt).all()
        result = []
        if not current_products:
            return {}
        for prod in current_products:
            prod_params = {
                "id": prod.id,
                "name": prod.name,
                "category": prod.category,
            }
            result.append(prod_params)
        return result
