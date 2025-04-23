from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.services.fetch_post import fetch_post_id
from app.states.post_states import GetPostState
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.utils.show_text import show_text
from app.utils.post_helpers import normalize_and_save_posts

router = Router()


@router.callback_query(F.data == "get_post_by_id")
async def ask_post_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите номер поста (только цифры):")
    await state.set_state(GetPostState.waiting_for_post_id)
    print("👉 Состояние установлено:", await state.get_state())  # ← вот это важно!





@router.message(GetPostState.waiting_for_post_id)
async def process_post_id(message: Message, state: FSMContext):
    async with SessionLocal() as session:

        if not message.text.isdigit():
            await message.answer("❗ Введите число.")
            return
    
        post_id = int(message.text)

        await state.clear()
        print(post_id)
        rep = PostRepository(session)
        post_bd = await rep.get_post_by_id(post_id)
        if len(post_bd) > 0:
            text = show_text(post_bd)

        else:
            post = await fetch_post_id(post_id)
            if not post:
                await message.answer(f"❗Пост с номером {post_id} не найден ни в БД, ни в API.\nВведите другое число.\n")
            result = await normalize_and_save_posts([post], session, message)    
            
            text = result["all"]

        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔢  Другой номер", callback_data="get_post_by_id")],
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])

        await message.answer(text,reply_markup=buttons)
         




@router.message()
async def catch_all(message: Message, state: FSMContext):
    current = await state.get_state()
    print("👀 Состояние сейчас:", current)
    print("📩 Сообщение получено:", message.text)
