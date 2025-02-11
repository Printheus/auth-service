import os
from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest_asyncio
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from auth_service.main import app, get_db
from auth_service.core.models import Base


@pytest_asyncio.fixture()
async def mock_db():
    db_conf = {"database": "test.sqlite3", "drivername": "sqlite+aiosqlite"}
    engine = create_async_engine(
        sa.URL.create(**db_conf),
        poolclass=sa.AsyncAdaptedQueuePool,
        echo=True,
        pool_size=20,
        max_overflow=0,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    LocalSession = async_sessionmaker(engine, expire_on_commit=False)
    session = LocalSession()
    yield session
    await session.aclose()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    os.remove("test.sqlite3")

@pytest_asyncio.fixture()
async def client(mock_db):
    app.dependency_overrides[get_db] = lambda: mock_db
    with TestClient(app) as client:
        yield client
