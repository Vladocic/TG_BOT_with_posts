from aiogram.types import CallbackQuery, F
from aiogram import Router, F

router = Router()


@router.callback_query(F.data == '')
async def handle_show_more(callback:CallbackQuery):

