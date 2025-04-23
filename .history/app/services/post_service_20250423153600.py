# app/services/post_service.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def build_main_menu() -> InlineKeyboardMarkup:
    """
    Создаёт главное меню с кнопками управления постами.
    :return: InlineKeyboardMarkup с кнопками действий.
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📚 Все посты", callback_data="get_all_posts")],
            [InlineKeyboardButton(text="🎲 Случайный пост", callback_data="get_random_post")],
            [InlineKeyboardButton(text="🔢 Пост по номеру", callback_data="get_post_by_id")],
            [
                InlineKeyboardButton(text="➕ Добавить 📝", callback_data="create_post"),
                InlineKeyboardButton(text="🗑 Удалить ❌", callback_data="delete_post_by_id")
            ],
            [InlineKeyboardButton(text="💣 Удалить всё (необратимо)", callback_data="delete_all")]
        ]
    )