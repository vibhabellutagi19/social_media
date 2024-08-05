from fastapi import FastAPI

from app.routers import auth
from . import models
from .database import engine
from .routers import post, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
