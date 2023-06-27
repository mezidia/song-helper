from server.src.database import get_user
from server.src.schemas import UserInDB


def test_get_user_existing_user():
    # Test getting an existing user
    username = "johndoe"
    expected_user = UserInDB(
        username="johndoe",
        full_name="John Doe",
        email="johndoe@example.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        disabled=False,
    )
    assert get_user(username) == expected_user


def test_get_user_nonexistent_user():
    # Test getting a nonexistent user
    username = "janedoe"
    assert get_user(username) is None
