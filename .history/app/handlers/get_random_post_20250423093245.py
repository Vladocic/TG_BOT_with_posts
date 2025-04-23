from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router,F
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.services.fetch_post import fetch_random_post
from app.utils.keyboard_helpers import build_menu_keyboard
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
from aiogram.fsm.context import FSMContext

import random


router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_random_post(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    async with SessionLocal() as session:
        repo = PostRepository(session)
        posts = await repo.get_all_posts_id()

        if len(posts) > 5:
            random_id = random.choice(posts)
            post = await repo.get_post_by_id(random_id)
            text = show_text(post)

 
        else:
            posts = await fetch_random_post()

            result = await normalize_and_save_posts([posts], session, callback)

            text = result["all"]

        buttons = build_menu_2_buttons(text="🎲 Ещё случайный", callback_data="get_random_post")

        await callback.message.answer(text,reply_markup = buttons)


        


