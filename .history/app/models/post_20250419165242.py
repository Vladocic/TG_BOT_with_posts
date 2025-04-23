from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Post(Base):
    id: Mapped[int] = mapped_column()
    title
    body
    userId
