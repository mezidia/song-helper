from typing import Annotated

from dependencies import get_current_active_user
from fastapi import APIRouter, Depends
from schemas import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@router.patch("/update/", response_model=User)
async def update_user_me(
    current_user: Annotated[User, Depends(get_current_active_user)], user: User
):
    return user


@router.delete("/delete/", response_model=User)
async def delete_user(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@router.get("/{id}", response_model=User)
async def read_user(id: int):
    print(id)
    return {"full_name": "John Doe", "username": "johndoe"}


@router.get("/", response_model=list[User])
async def read_users():
    return [
        {"full_name": "John Doe", "username": "johndoe"},
        {"full_name": "John Doe", "username": "johndoe"},
    ]
