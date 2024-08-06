# Pydantic model refers to schema ( structure of response/request )
# This ensure that when a user wants to create a post, the request will only go through
# if it has a 'title' and 'content' in the body
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


# Response from api to use


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
