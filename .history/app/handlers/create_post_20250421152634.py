from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.repositories.post import PostRepository
from app.services.fetch_post import fetch_random_post
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
import random
from app.states.post_states import AddPostState
from app.database.session import SessionLocal


router = Router()


@router.callback_query(F.data == "create_post")
async def ask_post_title(callback:CallbackQuery, state:FSMContext):
    await state.set_state(AddPostState.waiwaiting_for_title)
    await callback.message.answer("Напишите заголовок:")



@router.message(AddPostState.waiwaiting_for_title)
async def process_post_id(message: Message, state: FSMContext):
    await state.update_data(title = message.text)
    await state.set_state(AddPostState.waiting_for_text)
    await message.answer("Теперь введите текст статьи")


@router.message(AddPostState.waiting_for_text)
async def process_body (message: Message, state:FSMContext):
    data = await state.get_data()
    title = data.get("title")
    body = message.text
    

    async with SessionLocal() as session:
        post = 
    # body = state.get_data(body)




