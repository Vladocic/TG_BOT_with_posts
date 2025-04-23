from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext


from app.states.post_states import GetPostState

router = Router()


@router.message(GetPostState.waiting_for_post_id)
async def process_post_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❗ Введите число.")
        return
    
    post_id = int(message.text)
    await state.clear()



@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите номер поста от 1 до 100:")
    await state.set_state(GetPostState.waiting_for_post_id)



