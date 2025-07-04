from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart


async def start (messgae: types.Message):
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📄 Получить пост",callback_data="get_post")],
            [InlineKeyboardButton(text="➕ Создать пост",callback_data="create_post")],
            [InlineKeyboardButton(text="🗑 Удалить пост",callback_data="delete_post")]
    ])
    await messgae.answer("👋 Привет! Выберите действие:")