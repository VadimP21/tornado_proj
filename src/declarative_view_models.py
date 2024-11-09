from multiprocessing.pool import worker
from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn

from database import BaseProj, Base


class Category(BaseProj):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    products: Mapped[List["Product"]] = relationship(back_populates="category")

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"


class Product(BaseProj):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    category_id: Mapped[int | None] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Category | None] = relationship(back_populates="products")

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r})"


class WorkersOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


