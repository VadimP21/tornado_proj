from prod_app.models import Product
from prod_app.settings import SessionFactory
from sqlalchemy import select


# stmt = insert(Product).values(name=name)
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
#     product_id = result.inserted_primary_key[0]
#     # print(result.keys())
#     return product_id

# stmt = select(User).options(selectinload(User.addresses)).order_by(User.id)- OneToMany
# stmt = (
# ...     select(Address)
# ...     .options(joinedload(Address.user, innerjoin=True))
# ...     .order_by(Address.id)
# ... ) - ManyTo

# stmt = (
# ...     select(Address)
# ...     .join(Address.user)
# ...     .where(User.name == "pkrabs")
# ...     .options(contains_eager(Address.user))
# ...     .order_by(Address.id)
# ... ) -

# a1 = Address(email_address="pearl.krabs@gmail.com")
# u1.addresses.append(a1)

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
