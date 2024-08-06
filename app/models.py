# every model represent a table in database

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
from .database import Base
from sqlalchemy.orm import relationship


# Responsible for defining the columns of our "posts" table within postgres
# Is used to query, CRU entries within database
class Post(Base):
    __tablename__ = "posts_v2"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User") # name of the model


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
