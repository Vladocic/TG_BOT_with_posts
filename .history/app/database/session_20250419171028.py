from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker
from os import getenv
from app.config import DATABASE_URL

DATABASE_URL = os.ge