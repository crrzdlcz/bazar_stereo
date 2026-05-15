from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


# engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/proweb")
engine = create_engine(
    "postgresql+psycopg2://postgres:12345@25.33.129.73:5432/proweb",
    client_encoding="utf-8",
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600,
)

# session = Session(engine)
# session = scoped_session(sessionmaker(bind=engine))
Session = scoped_session(sessionmaker(bind=engine))
