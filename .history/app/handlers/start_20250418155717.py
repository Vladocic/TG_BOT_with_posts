from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start (message: types.Message):
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📚 Все посты",callback_data="get_all_posts")],
            [InlineKeyboardButton(text="🎲 Случайный пост",callback_data="create_post")],
            [InlineKeyboardButton(text="🗑 Удалить пост",callback_data="delete_post")]
    ])

    await message.answer(
        "👋 Привет! Выберите действие:",
        reply_markup=buttons
    )