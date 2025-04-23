from aiogram.types import CallbackQuery, F
from aiogram import Router, F

router = Router()


@router.callback_query(F.data == "show_more", session = )
async def handle_show_more(callback:CallbackQuery):

