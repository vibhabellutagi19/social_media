from fastapi import Depends, HTTPException, status, APIRouter
from .. import utils
from .. import models, schema
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse
)
def create_user(user: schema.CreateUser, db: Session = Depends(get_db)):
    # hash the password - user.password

    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd
    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schema.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(models.User.id == id).first()

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} doesnt exists",
        )

    return found_user
