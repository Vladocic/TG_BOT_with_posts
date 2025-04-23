from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.fetch_post import fetch_post_id
from app.states.post_states import GetPostState
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.utils.is_number import is_number
from app.utils.keyboard_helpers import build_menu_2_buttons, build_menu_back_button
from app.utils.show_text import show_text
from app.utils.post_helpers import normalize_and_save_posts

router = Router()


@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "🔢 Пост по номеру".
    Устанавливает состояние FSM для ожидания ввода ID поста от пользователя
    и выводит запрос на ввод числа.
    :param callback: Объект CallbackQuery от Telegram.
    :param state: Контекст FSM-состояния пользователя.
    """
    await state.set_state(GetPostState.waiting_for_post_id)
    await callback.message.answer("Введите номер поста (только цифры):")






