from aiogram.types import CallbackQuery
from aiogram import Router

router = Router()


@ro
async def handle_get_post_by_id(callback: CallbackQuery):