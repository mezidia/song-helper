import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_get_current_user(client: TestClient, token: str):
    response = client.get(
        "/users/me/",
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
        "/users/me/",
        headers={"Authorization": "Bearer tokenJWTtoken"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}


def test_update_user(client: TestClient, token: str):
    response = client.patch(
        "/users/update/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "username": "johndoe",
            "email": "email@gmail.com",
            "full_name": "John Doe",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "email": "email@gmail.com",
        "full_name": "John Doe",
        "disabled": None,
    }


def test_delete_user(client: TestClient, token: str):
    response = client.delete(
        "/users/delete/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
    }


def test_get_all_users(client: TestClient):
    response = client.get(
        "/users/",
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user(client: TestClient):
    response = client.get(
        "/users/1",
    )
    assert response.status_code == 200
    assert response.json() == {
        "full_name": "John Doe",
        "username": "johndoe",
        "email": None,
        "disabled": None,
    }
