from datetime import datetime, timedelta

from jose import jwt
from pytest import approx

from server.src.authentication import (
    create_access_token,
    get_password_hash,
    verify_password,
)
from server.src.config import settings


def test_password_hashing():
    password = "testpassword"
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)


def test_create_access_token():
    data = {"sub": "123"}
    access_token = create_access_token(data)
    decoded_token = jwt.decode(
        access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    assert decoded_token["sub"] == data["sub"]
    assert "exp" in decoded_token


def test_create_access_token_with_expiration():
    data = {"sub": "123"}
    expires_delta = timedelta(minutes=30)
    access_token = create_access_token(data, expires_delta)
    decoded_token = jwt.decode(
        access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    assert decoded_token["sub"] == data["sub"]
    assert "exp" in decoded_token
    expiration = datetime.fromtimestamp(decoded_token["exp"])
    date_now = datetime.utcnow()
    assert (expiration - date_now).total_seconds() == approx(
        expires_delta.total_seconds(), abs=1
    )
