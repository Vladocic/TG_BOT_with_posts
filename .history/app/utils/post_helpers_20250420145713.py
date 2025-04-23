from aiogram.types import CallbackQuery
from app.utils.case_converter import camel_to_snake_case



async def normalize_and_save_posts(posts: list[dict], session, callback: CallbackQuery) -> str | None:
    posts = camel_to_snake_case(posts)

    pass