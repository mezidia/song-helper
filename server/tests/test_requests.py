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
    assert response.json() == {
        "text": "test request",
        "id": 1,
        "user_id": 1,
        "answer": "Your request has been received",
    }


def test_get_requests(client: TestClient):
    response = client.get(
        "/requests/",
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "text": "test request",
            "id": 1,
            "user_id": 1,
            "answer": "Your request has been received",
        }
    ]


def test_get_requests_by_id(client: TestClient):
    response = client.get(
        "/requests/1/",
    )
    assert response.status_code == 200
    assert response.json() == {
        "text": "test request",
        "id": 1,
        "user_id": 1,
        "answer": "Your request has been received",
        "user": {
            "name": "johndoe",
            "email": "string",
            "disabled": False,
            "id": 1,
        },
    }


def test_get_requests_by_id_not_found(client: TestClient):
    response = client.get(
        "/requests/2/",
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Request not found"}


def test_update_request(client: TestClient, token: str):
    response = client.patch(
        "/requests/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "updated request", "user_id": 2},
    )
    assert response.status_code == 200
    assert response.json() == {
        "text": "updated request",
        "id": 1,
        "user_id": 2,
        "answer": "Your request has been received",
    }


def test_update_request_by_another_author(client: TestClient, token: str):
    response = client.patch(
        "/requests/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "updated request"},
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not enough permissions"}


def test_update_request_not_found(client: TestClient, token: str):
    response = client.patch(
        "/requests/2",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "updated request"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Request not found"}


def test_delete_request(client: TestClient, token: str):
    _ = client.post(
        "/requests/",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "test request"},
    )
    response = client.delete(
        "/requests/2",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Request deleted"}


def test_delete_request_by_another_author(client: TestClient, token: str):
    response = client.delete(
        "/requests/1",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Not enough permissions"}


def test_delete_request_not_found(client: TestClient, token: str):
    response = client.delete(
        "/requests/2",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Request not found"}
