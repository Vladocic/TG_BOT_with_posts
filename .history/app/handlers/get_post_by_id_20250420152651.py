from ssl import SSLContext
from aiogram.types import CallbackQuery
from aiogram import Router,F

router = Router()





@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: SSLContext):
    await callback.message.answer("Введите номер поста от 1 до 100:")
    await state.set_state(GetPostState.waiting_for_post_id)