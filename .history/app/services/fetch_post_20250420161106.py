import aiohttp
import random

async def fetch_all_posts() -> list[dict]:
    url = "https://jsonplaceholder.typicode.com/posts"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"❌ Ошибка запроса: {response.status}")
            return await response.json()



async def fetch_random_post() -> dict:
    all_posts = await fetch_all_posts()
    return random.choice(all_posts)
    

async def ferch_podt_id() -> dict|None:
    all_posts = await fetch_all_posts