from aiogram.types import CallbackQuery
from aiogram import Router,F

router = Router()


@router.callback_query(F.data == "get_post_by_id" )
async def handle_get_post_by_id(callback: CallbackQuery):
    pass


