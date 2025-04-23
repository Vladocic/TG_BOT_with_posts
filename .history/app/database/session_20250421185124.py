from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
        

from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session_factory() -> Callable[[], AsyncSession]:
    async def _get() -> AsyncSession:
        async with SessionLocal() as session:
            yield session
    return _get        