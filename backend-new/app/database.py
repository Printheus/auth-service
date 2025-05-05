from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker
import sqlalchemy as sa
from .settings import settings


engine = create_engine(
    sa.URL.create(**settings.DATABASE),
    poolclass=sa.QueuePool, 
    echo=False,
    pool_size=20,
    max_overflow=0
)


class Base(DeclarativeBase, MappedAsDataclass): ...

LocalSession = sessionmaker(bind=engine, expire_on_commit=False)

def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close() 