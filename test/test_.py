from fastapi.testclient import TestClient
from auth_service.main import app, get_db
from .mock import mock_db, client
from auth_service.core.controllers import UserController, schema
import pytest


def test_client(client: TestClient):
    res = client.post(
        "/",
        json={
            "username": "string",
            "password": "string",
        },
    )
    assert res.status_code == 200, res.content


@pytest.mark.asyncio
async def test_create_user(mock_db):
    data = schema.UserCreate(username="test", password="test123")
    user = await UserController(mock_db).create(data)
    assert user is not None
