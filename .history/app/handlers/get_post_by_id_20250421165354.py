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
    await state.set_state(GetPostState.waiting_for_post_id)
    await callback.message.answer("Введите номер поста (только цифры):")



@router.message(GetPostState.waiting_for_post_id)
async def process_post_id(message: Message, state: FSMContext):

    if not message.text.isdigit():
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])
        await message.answer("❗ Введите число.", reply_markup=button)
        return

    post_id = int(message.text)

    async with SessionLocal() as session:
        rep = PostRepository(session)
        post_bd = await rep.get_post_by_id(post_id)
        if len(post_bd) > 0:
            text = show_text(post_bd)

        else:
            post = await fetch_post_id(post_id)
            if not post:
                button = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
                ])
                await message.answer(f"❗Пост с номером {post_id} не найден ни в БД, ни в API.\nВведите другое число.\n", reply_markup=button)
                await state.set_state(GetPostState.waiting_for_post_id)
                return
            
            result = await normalize_and_save_posts([post], session, message)    
            
            text = result["all"]

        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔢  Другой номер", callback_data="get_post_by_id")],
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])

        await message.answer(text,reply_markup=buttons)
        await state.clear() 




