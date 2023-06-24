from fastapi.testclient import TestClient


def test_get_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.url == "http://testserver/docs"
