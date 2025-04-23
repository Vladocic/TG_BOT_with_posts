from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.repositories.post import PostRepository
from app.services.post_service import delete_all_posts_service
from app.states.post_states import AllDeleteState
from app.database.session import SessionLocal
from app.utils.keyboard_helpers import build_menu_back_button

router = Router()


@router.callback_query(F.data == "delete_all")
async def delete_all_posts(callback:CallbackQuery, state:FSMContext):
    """
    Обработчик кнопки "Удалить всё".
    Запрашивает у пользователя подтверждение действия.
    Устанавливает состояние ожидания текстового подтверждения удаления всех записей.
    """
    await callback.message.answer("Вы действительно хотите все удалить? Напшиите 'Да'")
    await state.set_state(AllDeleteState.waiting_for_all_delete)


@router.message(AllDeleteState.waiting_for_all_delete)
async def aprove_delete(message: Message, state: FSMContext):
    """
    Обрабатывает подтверждение удаления всех постов.
    Если подтверждение получено — удаляет все посты из базы и Google Таблицы.
    """
    correct_answer = ['да', 'Да', 'ok', 'yes', 'Yes']
    button = build_menu_back_button()

    if message.text not in correct_answer:
        await message.answer("Вы не подтвердили удаление, напищите 'Да', еще раз", reply_markup=button)
        return

    async with SessionLocal() as session:
        result = await delete_all_posts_service(session)

    text = '✅ Все данные удалены' if result else '⚠️ Удаления не произошло, таблица была пуста.'
    await message.answer(text, reply_markup=button)
    await state.clear()