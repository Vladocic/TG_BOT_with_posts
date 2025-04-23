from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router,F
from pydantic import ValidationError
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.schemas.post import PostSchema
from app.services.fetch_post import fetchall_posts, fetch_random_post
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
import random


router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        posts_ids = await repo.get_all_posts_id()

        if len(posts_ids) > 5:
            random_id = random.choice(posts_ids)
            post = await repo.get_post_by_id(random_id)
            text = show_text(post)

 
        else:
            posts = await fetch_random_post()

            result = await normalize_and_save_posts([posts], session, callback)

            text = result["all"]


        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🎲 Ещё случайный", callback_data="get_random_post")],
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])

        await callback.message.answer(text,reply_markup = button)


        


