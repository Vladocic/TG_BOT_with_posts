from aiogram.types import CallbackQuery
from aiogram import Router,F
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
import math


router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        posts_ids = await repo.get_all_posts_id()
        if len(posts_ids) == 0:
            pass
        
        posts_ids.c
        print(posts_count)
        math.radians

        
        
        # if repo is None:

        # else:

        # get_count_all_posts()
        # pass



