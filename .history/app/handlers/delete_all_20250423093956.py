from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.repositories.post import PostRepository
from app.states.post_states import AllDeleteState
from app.database.session import SessionLocal
from app.utils.keyboard_helpers import build_menu_back_button

router = Router()


@router.callback_query(F.data == "delete_all")
async def delete_all_posts(callback:CallbackQuery, state:FSMContext):
    await callback.message.answer("Вы действительно хотите все удалить? Напшиите 'Да'")
    await state.set_state(AllDeleteState.waiting_for_all_delete)


@router.message(AllDeleteState.waiting_for_all_delete)
async def aprove_delete(message:Message, state:FSMContext):
    correct_answer = ['да', 'Да', 'ok', 'yes', 'Yes']
    button = build_menu_back_button()

    if message.text not in correct_answer:
        await message.answer("Вы не подтвердили удаление, напищите 'Да', еще раз", reply_markup= button)
        return

    async with SessionLocal() as session:
        repo = PostRepository(session)
        result = await repo.del_all_posts()

        text = '✅ Все данные удалены' if result else '⚠️ Удаления не прозошло, таблица была пуста.'
        await message.answer(text, reply_markup=button)
        await state.clear()