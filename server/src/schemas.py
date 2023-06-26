from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class RequestBase(SQLModel):
    text: str


class Request(RequestBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: "User" = Relationship(back_populates="requests")
    user_id: int = Field(default=None, foreign_key="user.id")


class RequestCreate(RequestBase):
    pass


class RequestRead(RequestBase):
    id: int
    user_id: int


class RequestUpdate(SQLModel):
    text: Optional[str] = None
    user_id: Optional[int] = None


class UserBase(SQLModel):
    name: str = Field(index=True, unique=True)
    email: str
    disabled: bool = False


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str = Field()
    requests: Optional[list[Request]] = Relationship(back_populates="user")


class UserRead(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class RequestReadWithUser(RequestRead):
    user: Optional[UserRead] = None


class UserReadWithRequests(UserRead):
    requests: Optional[list[RequestRead]] = None


class Prompt(BaseModel):
    prompt: str
