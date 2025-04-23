from aiogram.types import CallbackQuery
from aiogram import Router, F
from app.handlers.start import start
from aiogram.fsm.context import FSMContext


router = Router()

@router.callback_query(F.data == "back_to_menu")
async def handle_back_to_menu(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "В меню".

    Завершает текущее состояние FSM и вызывает стартовое меню.

    :param callback: Объект CallbackQuery от пользователя.
    :param state: Контекст текущего состояния FSM.
    """
    await state.clear()
    await start(callback.message, state)