import pytest_asyncio, pytest

from .mock import client, mock_db, TestClient
from auth_service.core.controllers import UserController, schema


@pytest_asyncio.fixture()
async def mock_user(mock_db):
    data = schema.UserCreate(username="valid_user", password="hashed_password")
    user = await UserController(mock_db).create(data)
    return user


def login(client, username: str, password: str):
    response = client.post("/login", json={"username": username, "password": password})
    return response


def test_login_successful(client: TestClient, mock_user):
    response = login(client, mock_user.username, "hashed_password")
    assert response.status_code == 200, response.content
    assert "Access-Token" in response.cookies


def test_login_wrong_password(client, mock_user):
    """Test login with correct username but wrong password"""
    response = login(client, "valid_user", "wrongpassword")
    assert response.status_code == 401


def test_login_wrong_username(client, mock_user):
    """Test login with wrong username"""
    response = login(client, "wronguser", "password123")
    assert response.status_code == 401


def test_login_empty_username(client, mock_user):
    response = login(client, "", "password123")
    assert response.status_code == 401


def test_login_empty_password(client, mock_user):
    """Test login with empty password"""
    response = login(client, "valid_user", "")
    assert response.status_code == 401


def test_login_empty_credentials(client, mock_user):
    """Test login with empty username and password"""
    response = login(client, "", "")
    assert response.status_code == 401


def test_login_sql_injection(client, mock_user):
    response = login(client, "valid_user' OR '1'='1", "password")
    assert response.status_code == 401


@pytest.mark.skip()
def test_login_brute_force_protection(client, mock_user):
    for _ in range(5):  # Simulate 5 failed login attempts
        response = login(client, "valid_user", "wrong_password")
        assert response.status_code == 401

    response = login(client, "valid_user", "hashed_password")
    assert response.status_code == 429


async def test_login_xss_attack(client):
    """Test XSS Attack attempt"""
    response = login(client, "<script>alert('XSS')</script>", "password123")
    assert response.status_code == 401
