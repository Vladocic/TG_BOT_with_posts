from aiogram.types import CallbackQuery
from app.services.


async def handle_get_all_posts(callback:CallbackQuery):
    if callback.data == "get_all_posts":
        print(callback)
