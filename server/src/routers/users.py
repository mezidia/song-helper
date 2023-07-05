from typing import Annotated

from database import get_session
from dependencies import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException, Query, status
from schemas import User, UserRead, UserReadWithRequests, UserUpdate
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@router.patch(
    "/update/", response_model=UserRead, status_code=status.HTTP_200_OK
)
async def update_user_me(
    *,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
    user: UserUpdate,
):
    user_id = current_user.id
    db_user = session.get(User, user_id)
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.delete("/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    *,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: Session = Depends(get_session),
):
    user_id = current_user.id
    db_user = session.get(User, user_id)
    session.delete(db_user)
    session.commit()
    return


@router.get(
    "/{id}",
    response_model=UserReadWithRequests,
    status_code=status.HTTP_200_OK,
)
async def read_user(*, session: Session = Depends(get_session), id: int):
    if user := session.get(User, id):
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def read_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.query(User).offset(offset).limit(limit).all()
    return users
