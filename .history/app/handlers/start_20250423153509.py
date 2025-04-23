from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from app.services.post_service import build_main_menu


async def start (message: types.Message, state: FSMContext):
    """
    Обрабатывает команду /start и возвращает главное меню с кнопками управления постами.
    Очищает текущее состояние пользователя и показывает интерфейс с действиями:
    - Просмотр всех постов
    - Получение случайного поста
    - Получение поста по номеру
    - Добавление нового поста
    - Удаление поста по ID
    - Полное удаление всех постов
    :param message: Объект входящего сообщения от Telegram.
    :param state: Контекст FSM-состояния пользователя.
    """
    await state.clear()
    build_main_menu()
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📚 Все посты",callback_data="get_all_posts")],
            [InlineKeyboardButton(text="🎲 Случайный пост",callback_data="get_random_post")],
            [InlineKeyboardButton(text="🔢 Пост по номеру",callback_data="get_post_by_id")],
            [
                InlineKeyboardButton(text="➕ Добавить 📝",callback_data="create_post"), 
                InlineKeyboardButton(text="🗑 Удалить ❌",callback_data="delete_post_by_id"),
            ],
            [InlineKeyboardButton(text="💣 Удалить всё (необратимо)",callback_data="delete_all")]
    ])

    await message.answer(
        "👋 Привет! Выберите действие:",
        reply_markup=buttons
    )