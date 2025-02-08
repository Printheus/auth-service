from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
import sqlalchemy as sa
from .config_manager import conf


engine = create_async_engine(
    sa.URL.create(**conf.db_conf),
    echo=False,
    pool_size=20,
    max_overflow=0
)


class Base(DeclarativeBase, MappedAsDataclass): ...

LocalSession = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        await session.close()