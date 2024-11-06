from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite+pysqlite:///sqlite.db"

engine = create_engine(DB_URL, echo=True)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
