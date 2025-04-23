from aiogram.types import CallbackQuery, F
from aiogram import Router, F
from app.database.session import SessionLocal
from app.repositories.post import PostRepository,get_posts_paginated

router = Router()


@router.callback_query(F.data == "show_more")
async def handle_show_more(callback:CallbackQuery):
    if callback.data.startswith("show_more:"):
        offset = int(callback.data.split(":")[1])
        get_posts_paginated()
        pass



        stmt = insert(Post).values(post_dicts).on_conflict_do_nothing(index_elements=['id'])
