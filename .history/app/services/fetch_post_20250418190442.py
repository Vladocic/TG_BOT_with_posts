import aiohttp


async def fetch_all_posts() -> list[dict]:
    url = "https://jsonplaceholder.typicode.com/posts"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            raise Exception(f"❌ Ошибка запроса: {response.status})
