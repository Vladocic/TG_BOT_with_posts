from dotenv import load_dotenv
import os
import asyncio
import asyncpg

load_dotenv()

async def test_conn():
    db_url = os.getenv("DATABASE_URL")
    print("Trying to connect to:", db_url)
conn = await asyncpg.connect("postgres://postgres:postgres@localhost:5432/my_bot")    print("✅ Connected!")
    await conn.close()

asyncio.run(test_conn())