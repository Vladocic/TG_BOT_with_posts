import asyncio
from app.database.session import engine
from app.models.base import Base
from app.models.post import Post  # чтобы SQLAlchemy знал про таблицу


async def init_db():
    await wait_for_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Таблицы созданы")

if __name__ == "__main__":
    asyncio.run(init_db())