from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from app.models.base import Base

class Base(DeclarativeBase):
    pass