import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_request(client: TestClient, token: str):
    response = client.post(
        "/requests/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"full_name": "John Doe", "username": "johndoe"}


def test_get_requests_by_id(client: TestClient):
    response = client.get(
        "/requests/3/",
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0] == {
        "full_name": "John Doe",
        "username": "johndoe",
        "id": 3,
    }


def test_delete_request(client: TestClient, token: str):
    response = client.delete(
        "/requests/delete/3",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == 3
