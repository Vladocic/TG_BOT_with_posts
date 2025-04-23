from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker
from os import getenv
from app.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=
)