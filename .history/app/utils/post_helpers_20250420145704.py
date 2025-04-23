from aiogram.types import CallbackQuery



async def normalize_and_save_posts(posts: list[dict], session, callback: CallbackQuery) -> str | None:
                posts = camel_to_snake_case(posts)

    pass