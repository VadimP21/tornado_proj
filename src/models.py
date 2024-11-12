import datetime
import enum
from typing import List, Annotated

from sqlalchemy import String, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn

from database import BaseProj, Base, str_255

# Переиспользование типов на уровне модуля
int_pk_type = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at_type = Annotated[
    datetime.datetime,
    mapped_column(primary_key=True, server_default=text("TIMEZONE('utc',now())")),
]  # sql query вставка текущего времени на уровне БД
updated_at_type = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc',now())"), onupdate=datetime.datetime.utcnow
    ),
]


class WorkersOrm(Base):
    __tablename__ = "workers"
    id: Mapped[int_pk_type]
    username: Mapped[str_255]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"
    id: Mapped[int_pk_type]
    title: Mapped[str_255]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]
