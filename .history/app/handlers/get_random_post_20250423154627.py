from aiogram.types import CallbackQuery
from aiogram import Router,F
from app.database.session import SessionLocal
from app.services.post_service import get_random_post_text
from app.utils.keyboard_helpers import build_menu_2_buttons
from aiogram.fsm.context import FSMContext
import random

router = Router()

@router.callback_query(F.data == "get_random_post")
async def handle_random_post(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "🎲 Случайный пост".
    Если в базе данных уже есть более 5 постов, выбирается случайный из них.
    Иначе — выполняется запрос к внешнему API, полученный пост сохраняется
    в базу данных и выводится пользователю.
    :param callback: Объект CallbackQuery от Telegram.
    :param state: Контекст FSM-состояния пользователя.
    """
    await state.clear()
    async with SessionLocal() as session:
        text = await get_random_post_text(session, callback)

        buttons = build_menu_2_buttons("🎲 Ещё случайный", "get_random_post")
        await callback.message.answer(text, reply_markup=buttons)


        


