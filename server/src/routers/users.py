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


@router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]
