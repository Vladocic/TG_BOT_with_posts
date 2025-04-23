from aiogram import types
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
    buttons = build_main_menu()

    await message.answer(
        "👋 Привет! Выберите действие:",
        reply_markup=buttons
    )