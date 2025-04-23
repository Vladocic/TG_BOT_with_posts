from aiogram.types import CallbackQuery
from aiogram import Router, F


@router.callback_query(F.data == "back_to_menu")
async def handle_back_to_menu(callback: CallbackQuery):
    await start(callback.message)