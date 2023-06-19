import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/token", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_fail_login(client: TestClient):
    response = client.post(
        "/token", data={"username": "john", "password": "changeme"}
    )
    assert response.json() == {"detail": "Incorrect username or password"}
    assert response.status_code == 401


def test_login(client: TestClient):
    response = client.post(
        "/token", data={"username": "johndoe", "password": "secret"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    token = response.json()["access_token"]
    assert token is not None


def test_get_current_user(client: TestClient, token: str):
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
    }


def test_fail_get_current_user(client: TestClient):
    response = client.get(
        "/users/me",
        headers={"Authorization": "Bearer tokenJWTtoken"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}


def test_get_current_user_items(client: TestClient, token: str):
    print(token)
    response = client.get(
        "/users/me/items",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == [{"item_id": "Foo", "owner": "johndoe"}]
