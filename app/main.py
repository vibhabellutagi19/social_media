from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import Settings
from app.routers import auth, vote
from .routers import post, users


app_settings = Settings()
origins = [
    "https://www.google.com/",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)
