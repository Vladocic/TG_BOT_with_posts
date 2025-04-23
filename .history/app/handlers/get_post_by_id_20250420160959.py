from aiogram.types import CallbackQuery, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.fetch_post import fetch_all_posts
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
        post = await rep.get_post_by_id(post_id)
        if len(post) > 0:
            text = show_text(post)

        else:
            posts = await fetch_all_posts()
            try:
                p
            pass





        await state.clear()



@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите номер поста (только цифры):")
    await state.set_state(GetPostState.waiting_for_post_id)



