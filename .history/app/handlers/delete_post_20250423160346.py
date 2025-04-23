from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.post_service import delete_post_by_id_service
from app.states.post_states import DeletePostState
from app.database.session import SessionLocal
from app.utils.is_number import is_number
from app.utils.keyboard_helpers import build_menu_2_buttons,is


router = Router()

@router.callback_query(F.data == "delete_post_by_id")
async def handle_delete_post(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Удалить пост по ID".
    Устанавливает состояние ожидания ввода ID поста от пользователя.
    """
    await state.set_state(DeletePostState.waiting_for_post_id)
    await callback.message.answer("Введите ID поста для удаления:")


@router.message(DeletePostState.waiting_for_post_id)
async def ask_post_id_to_delete(message: Message, state: FSMContext):
    """
    Обрабатывает сообщение с ID поста от пользователя.
    Проверяет корректность ID и удаляет соответствующий пост из базы и Google Таблицы.
    """
    if not await is_number(message):
        return

    post_id = int(message.text)

    async with SessionLocal() as session:
        deleted = await delete_post_by_id_service(post_id, session)

    text = f"✅ Пост с ID {post_id} удалён." if deleted else f"❗ Пост с ID {post_id} не найден."
    buttons = build_menu_2_buttons(text="❌ Удалить еще пост", callback_data="delete_post_by_id")

    await state.clear()
    await message.answer(text, reply_markup=buttons)


    
    
 