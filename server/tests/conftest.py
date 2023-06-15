from typing import Generator

import pytest
from fastapi.testclient import TestClient

from server.src.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def token(client: TestClient) -> str:
    pass
