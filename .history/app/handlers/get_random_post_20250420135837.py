from aiogram.types import CallbackQuery
from aiogram import Router,F
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
import random

from app.utils import show_text


router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        posts_ids = await repo.get_all_posts_id()

        if len(posts_ids) > 0:
            random_id = random.choice(posts_ids)
            post = await repo.get_post_by_id(random_id)
            text = show_text(post)

            await callback.message.answer(text)
  

        


