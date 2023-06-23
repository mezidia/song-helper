import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_register(client: TestClient):
    response = client.post(
        "/register",
        json={
            "username": "johndoe",
            "hashed_password": "string",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "johndoe"
    assert data["email"] is None
    assert data["full_name"] is None


def test_fail_register(client: TestClient):
    response = client.post(
        "/register",
        json={"username": "johndoe"},
    )
    assert response.status_code == 422


def test_fail_login(client: TestClient):
    response = client.post(
        "/login", data={"username": "john", "password": "changeme"}
    )
    assert response.json() == {"detail": "Incorrect username or password"}
    assert response.status_code == 401


def test_login(client: TestClient):
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    token = response.json()["access_token"]
    assert token is not None
