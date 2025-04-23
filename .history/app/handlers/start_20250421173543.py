from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext


async def start (message: types.Message, state: FSMContext):
    await state.clear()
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📚 Все посты",callback_data="get_all_posts"),
            InlineKeyboardButton(text="🎲 Случайный пост",callback_data="get_random_post"),
            InlineKeyboardButton(text="🔢 Пост по номеру",callback_data="get_post_by_id") 
            ],

            [
                InlineKeyboardButton(text="➕ Добавить 📝",callback_data="create_post"), 
                InlineKeyboardButton(text="🗑 Удалить ❌",callback_data="delete_post")
            ]
    ])

    await message.answer(
        "👋 Привет! Выберите действие:",
        reply_markup=buttons
    )