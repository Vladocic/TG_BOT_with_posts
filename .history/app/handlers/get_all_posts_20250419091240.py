from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from app.services.fetch_post import fetch_all_posts


async def handle_get_all_posts(callback:CallbackQuery):
    if callback.data == "get_all_posts":
        print(callback)
        posts = await fetch_all_posts()
        five_posts = posts[0:5]
        buttons = 



        # for posts in 
