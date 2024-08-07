from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schema, utils
import app.oauth2 as oauth2

from ..database import get_db

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=schema.AccessToken)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
    # OAuth2PasswordRequestForm will return username= and password=

    login_user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not login_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    if not utils.is_password_exists(user_credentials.password, login_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    # create a token
    access_token = oauth2.create_access_token(data = {"user_id": login_user.id})

    # return token
    return {"access_token": access_token, "token_type": "bearer"}
