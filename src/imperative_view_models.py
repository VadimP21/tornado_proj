from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()


product_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

