import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    response = client.post(
        "/login", data={"username": "johndoe", "password": "secret"}
    )
    token = response.json()["access_token"]
    return token


def test_create_prompt(client: TestClient, token: str):
    response = client.post(
        "/prompt/new/",
        headers={"Authorization": f"Bearer {token}"},
        params={"prompt": "Test Prompt"},
    )
    assert response.status_code == 200
    assert response.json() == "Test Prompt"
