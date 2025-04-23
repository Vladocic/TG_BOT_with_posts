import asyncio
from app.database.session import engine
from app.models.base import Base
from app.models.post import Post  # чтобы SQLAlchemy знал про таблицу


async def init_db():
    await wait_for_db()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Таблицы созданы")

async def wait_for_db():
    for i in range(10):
        try:
            conn = await asyncpg.connect("postgresql://postgres:postgres@db:5432/my_bot")
            await conn.close()
            print("✅ БД доступна!")
            return
        except Exception as e:
            print(f"⏳ Ожидание БД... попытка {i + 1}")
            await asyncio.sleep(2)
    raise Exception("❌ БД не запустилась.")



if __name__ == "__main__":
    asyncio.run(init_db())