from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.post_service import get_post_by_id_text
from app.states.post_states import GetPostState
from app.database.session import SessionLocal
from app.utils import build_menu_2_buttons, build_menu_back_button, is_number

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



@router.message(GetPostState.waiting_for_post_id)
async def process_post_id(message: Message, state: FSMContext):
    """
    Обрабатывает введённый пользователем ID поста.
    """
    if not await is_number(message):
        return

    post_id = int(message.text)

    async with SessionLocal() as session:
        text, found = await get_post_by_id_text(post_id, session, message)

        if not found:
            button = build_menu_back_button()
            await message.answer(f"❗Пост с номером {post_id} не найден ни в БД, ни в API.\nВведите другое число.\n", reply_markup=button)
            await state.set_state(GetPostState.waiting_for_post_id)
            return

        buttons = build_menu_2_buttons("🔢 Другой номер", "get_post_by_id")
        await message.answer(text, reply_markup=buttons)
        await state.clear()


