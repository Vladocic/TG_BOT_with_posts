from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.repositories.post import PostRepository
from app.states.post_states import DeletePostState, AllDeleteState
from app.database.session import SessionLocal
from app.utils.is_number import is_number
from app.utils.keyboard_helpers import build_menu_keyboard


router = Router()

@router.callback_query(F.data == "delete_post_by_id")
async def handle_delete_post(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DeletePostState.waiting_for_post_id)
    await callback.message.answer("Введите ID поста для удаления:")

@router.message(DeletePostState.waiting_for_post_id)
async def ask_post_id_to_delete(message:Message, state: FSMContext):
    if not await is_number(message):
        return
    post_id = int(message.text)

    async with SessionLocal() as session:
        repo = PostRepository(session)
        deleted = await repo.del_post_by_id(post_id)


        text = f"✅ Пост с ID {post_id} удалён." if deleted else f"❗ Пост с ID {post_id} не найден."
        await state.clear()

        buttons = build_menu_keyboard()

        buttons = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="❌ Удалить еще пост", callback_data="delete_post_by_id")],
                [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
            ])

        await message.answer(text, reply_markup=buttons )


    
    
 