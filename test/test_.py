from fastapi.testclient import TestClient
from auth_service.main import app, get_db
from .mock import mock_db, client
from auth_service.core.controllers import UserController, AsyncSession, User
import sqlalchemy as sa
import pytest


@pytest.mark.asyncio
async def test_create_user(mock_db: AsyncSession):
    data = {"username": "test", "password": "test123"}
    user = await UserController(mock_db).create(data)
    assert user is not None
    query = sa.select(User).where(User.user_id == user.user_id)
    res = await mock_db.scalars(query)
    user_db = res.first()
    assert user_db is not None


@pytest.mark.asyncio
async def test_hash_passwd(mock_db):
    data = {"username": "test", "password": "test123"}
    user = await UserController(mock_db).create(data)
    assert user is not None, "Failed to create user"
    assert user.password is not None, "Password is None"
    assert user.password != "test123", f"password is plaintext password"
    assert user.password.startswith("$2b$"), "password is not of type bcrypt"
