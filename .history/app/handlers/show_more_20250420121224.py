from aiogram.types import CallbackQuery
from aiogram import Router

router = Router()


@router.callback_query()
async def handle_show_more(callback:CallbackQuery):

