from typing import Annotated

from database import get_session
from dependencies import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException, Query, status
from schemas import (
    Request,
    RequestCreate,
    RequestRead,
    RequestReadWithUser,
    RequestUpdate,
    User,
)
from sqlmodel import Session, select

router = APIRouter(prefix="/requests", tags=["requests"])


@router.post(
    "/", response_model=RequestRead, status_code=status.HTTP_201_CREATED
)
def create_request(
    *,
    session: Session = Depends(get_session),
    current_user: Annotated[User, Depends(get_current_active_user)],
    request: RequestCreate,
):
    db_request = Request(
        text=request.text,
        user_id=current_user.id,
        answer="Your request has been received",
    )
    session.add(db_request)
    session.commit()
    session.refresh(db_request)
    return db_request


@router.get(
    "/", response_model=list[RequestRead], status_code=status.HTTP_200_OK
)
def read_requests(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    requests = session.exec(select(Request).offset(offset).limit(limit)).all()
    return requests


@router.get(
    "/{request_id}",
    response_model=RequestReadWithUser,
    status_code=status.HTTP_200_OK,
)
def read_request(*, request_id: int, session: Session = Depends(get_session)):
    request = session.get(Request, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request


@router.patch(
    "/{request_id}", response_model=RequestRead, status_code=status.HTTP_200_OK
)
def update_request(
    *,
    session: Session = Depends(get_session),
    request_id: int,
    request: RequestUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    db_request = session.get(Request, request_id)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    if db_request.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    request_data = request.dict(exclude_unset=True)
    for key, value in request_data.items():
        setattr(db_request, key, value)
    session.add(db_request)
    session.commit()
    session.refresh(db_request)
    return db_request


@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_request(
    *,
    session: Session = Depends(get_session),
    current_user: Annotated[User, Depends(get_current_active_user)],
    request_id: int,
):
    request = session.get(Request, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    if request.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    session.delete(request)
    session.commit()
    return {"message": "Request deleted"}
