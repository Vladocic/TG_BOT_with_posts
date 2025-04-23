from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router,F
from pydantic import ValidationError
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.schemas.post import PostSchema
from app.services.fetch_post import fetch_all_posts, fetch_random_post
from app.utils.case_converter import camel_to_snake_case
from app.utils.show_text import show_text
import random


router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        posts_ids = await repo.get_all_posts_id()

        if len(posts_ids) > 0:
            random_id = random.choice(posts_ids)
            print(random_id)
            post = await repo.get_post_by_id(random_id)
            text = show_text(post)

            button = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
            ])

            await callback.message.answer(text, reply_markup=button)
  
        else:
            async with SessionLocal() as session:

                posts = await fetch_random_post()
                posts = camel_to_snake_case(posts)
            try:
                validated = [PostSchema(**post) for post in posts]
            except ValidationError as e:
                await callback.message.answer(f"❌ Ошибка валидации: {e}")
                return
            
            repo = PostRepository(session)

        


