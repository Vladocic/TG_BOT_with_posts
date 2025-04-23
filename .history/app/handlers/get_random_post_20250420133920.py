from aiogram.types import CallbackQuery
from aiogram import Router,F
from app.repositories.post import PostRepository
from app.database.session import SessionLocal

router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        repo.get_count_all_posts()
        
        
        
        if repo is None:

        else:

        get_count_all_posts()
        pass



