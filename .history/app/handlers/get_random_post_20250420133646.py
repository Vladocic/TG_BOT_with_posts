from aiogram.types import CallbackQuery
from aiogram import Router,F
from app.repositories.post import 
router = Router()


@router.callback_query(F.data == "get_random_post" )
async def handle_get_post_by_id(callback: CallbackQuery):

    get_count_all_posts()
    pass



