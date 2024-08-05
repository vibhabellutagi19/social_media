from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter

import oauth2


from .. import models, schema
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=List[schema.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(
    post: schema.CreatePost,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user),
):
    # user should be logged in to create the post
    print(current_user.email)
    new_post = models.Post(**post.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # like retrieve the new post and store it in new_post
    return new_post


# {id} is path parameter
@router.get("/{id}", response_model=schema.Post)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user),
):  # to vaidate the id always be int, provide it as int
    found_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not found_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    return found_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user),
):
    found_post = db.query(models.Post).filter(models.Post.id == id)

    if found_post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )
    found_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schema.Post)
def update_post(
    id: int,
    post: schema.PostBase,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user),
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_row = post_query.first()
    if post_row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    post_query.update(post.model_dump(), synchronize_session=False)

    db.commit()

    return post.model_dump()
