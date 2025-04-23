from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart


async def dd (messgae: types.Message):
    buttoms = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📄 Получить пост",callback_data="get_post"),
             InlineKeyboardButton(text="т",callback_data="create_post"),
             InlineKeyboardButton(text="❌ Удалить пост",callback_data="del_post")
             ]
    ])