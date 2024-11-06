from sqlalchemy import create_engine


database_url = "sqlite+pysqlite:///sqlite.db"
engine = create_engine(database_url, echo=True)
