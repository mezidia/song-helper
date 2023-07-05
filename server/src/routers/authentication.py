from datetime import timedelta
from typing import Annotated

from authentication import (
    create_access_token,
    get_password_hash,
    verify_password,
)
from config import settings
from database import get_session, get_user
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas import Token, User, UserCreate, UserRead
from sqlmodel import Session

router = APIRouter(tags=["authentication"])


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@router.post(
    "/register", response_model=UserRead, status_code=status.HTTP_201_CREATED
)
async def create_user(
    *, session: Session = Depends(get_session), user: UserCreate
):
    db_user = User(
        email=user.email,
        name=user.name,
        password=get_password_hash(user.password),
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
