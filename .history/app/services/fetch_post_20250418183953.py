import aiohttp


async def fetch_all_posts() -> list[dict]:
    url = "https://jsonplaceholder.typicode.com/posts"

    async with aiohttp.ClientS
