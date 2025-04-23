from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.models.post import Post
from app.repositories.post import PostRepository
from app.states.post_states import DeletePostState, AllDeleteState
from app.database.session import SessionLocal
from app.utils.is_number import is_number


router = Router()

@router.callback_query(F.data == "delete_post_by_id")
async def handle_delete_post(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DeletePostState.waiting_for_post_id)
    await callback.message.answer("Ввкдите ID поста для удаления:")

@router.message(DeletePostState.waiting_for_post_id)
async def ask_post_id_to_delete(message:Message, state: FSMContext):
    if not await is_number(message):
        return
    post_id = int(message.text)

    async with SessionLocal() as session:
        repo = PostRepository(session)
        await repo.del_post_by_id(post_id)


        deleted = await repo.delete_post_by_id(post_id)
        if deleted:
            await message.answer(f"✅ Пост с ID {post_id} удалён.")
        else:
            await message.answer(f"❗ Пост с ID {post_id} не найден.")
        pass

    
    
 