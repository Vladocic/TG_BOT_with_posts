import asyncio
from app.database.session import engine
from app.models.base import Base
from app.models.post import Post  # чтобы SQLAlchemy знал про таблицу

import os

async def init_db():
    print("DATABASE_URL:", os.getenv("DATABASE_URL"))

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Таблицы созданы")

if __name__ == "__main__":
    asyncio.run(init_db())