import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_create_request(client: TestClient, token: str):
    response = client.post(
        "/requests/",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "test request"},
    )
    assert response.status_code == 200
    assert response.json() == {"text": "test request", "id": 1, "user_id": 1}


def test_get_requests_by_id(client: TestClient):
    response = client.get(
        "/requests/1/",
    )
    assert response.status_code == 200
    assert response.json() == {
        "text": "test request",
        "id": 1,
        "user_id": 1,
        "user": {
            "name": "johndoe",
            "email": "string",
            "disabled": False,
            "id": 1,
        },
    }


def test_delete_request(client: TestClient, token: str):
    response = client.delete(
        "/requests/1",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Request deleted"}
