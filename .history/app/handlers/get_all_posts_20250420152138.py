from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F
from pydantic import ValidationError
from app.services.fetch_post import fetch_all_posts
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
from app.utils.case_converter import camel_to_snake_case
from app.repositories.post import PostRepository
from app.database.session import SessionLocal


router = Router()


@router.callback_query(F.data == "get_all_posts")
async def handle_get_all_posts(callback:CallbackQuery): 
        async with SessionLocal() as session:

            posts = await fetch_all_posts()

            result = await normalize_and_save_posts(posts, session, callback)

            text = result["preview"]
        

            button = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📩 Показать ещё", callback_data="show_more:5")],
                [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
            ])
            await callback.message.answer(text,reply_markup = button)


