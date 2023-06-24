from typing import Annotated

from dependencies import get_current_active_user
from fastapi import APIRouter, Depends
from schemas import User

router = APIRouter(prefix="/requests", tags=["requests"])


@router.delete("/delete/{id}")
async def delete_request(
    current_user: Annotated[User, Depends(get_current_active_user)], id: int
):
    return id


@router.post("/")
async def create_request(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return {
        "full_name": current_user.full_name,
        "username": current_user.username,
    }


@router.get("/{user_id}/")
async def read_requests(user_id: int):
    return [
        {"full_name": "John Doe", "username": "johndoe", "id": user_id},
        {"full_name": "John Doe", "username": "johndoe", "id": user_id},
    ]
