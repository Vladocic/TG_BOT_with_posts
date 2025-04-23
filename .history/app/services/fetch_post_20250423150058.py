import aiohttp
import random

async def fetch_all_posts() -> list[dict]:
    """
    Получает все посты с внешнего API JSONPlaceholder.
    :return: Список словарей, каждый из которых представляет пост.
    :raises Exception: Если API возвращает статус отличный от 200.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"❌ Ошибка запроса: {response.status}")
            return await response.json()



async def fetch_random_post() -> dict:
    """
    Получает случайный пост из API.
    :return: Один пост в виде словаря.
    """
    all_posts = await fetch_all_posts()
    return random.choice(all_posts)
    

async def fetch_post_id(id:int) -> dict|None:
    """
    Ищет пост по заданному ID в списке всех постов.
    :param id: Искомый ID поста.
    :return: Словарь поста, если найден. Иначе None.
    """
    all_posts = await fetch_all_posts()
    for post in all_posts:
        if post["id"] == id:
            return post
    return None    
