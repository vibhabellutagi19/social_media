# Pydantic model refers to schema ( structure of response/request )
# This ensure that when a user wants to create a post, the request will only go through
# if it has a 'title' and 'content' in the body
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


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


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True


class PostResponse(BaseModel):
    Post: Post
    votes: int


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class Vote(BaseModel):
    post_id: int
    direction_of_vote: int = Field(..., ge=0, le=1)


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
