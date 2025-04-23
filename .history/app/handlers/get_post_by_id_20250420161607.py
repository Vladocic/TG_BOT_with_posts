from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.fetch_post import fetch_all_posts, fetch_podt_id
from app.states.post_states import GetPostState
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.utils.case_converter import show_text

router = Router()


@router.message(GetPostState.waiting_for_post_id)
async def process_post_id(message: Message, state: FSMContext):
    async with SessionLocal() as session:

        if not message.text.isdigit():
            await message.answer("❗ Введите число.")
            return
    
        post_id = int(message.text)

        rep = PostRepository(session)
        post_bd = await rep.get_post_by_id(post_id)
        if len(post_bd) > 0:
            text = show_text(post_bd)

        else:
            post = await fetch_podt_id(post_id)
            if not post:
                await message.answer()

         




        await state.clear()



@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите номер поста (только цифры):")
    await state.set_state(GetPostState.waiting_for_post_id)



