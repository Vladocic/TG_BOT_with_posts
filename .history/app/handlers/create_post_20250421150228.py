from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.repositories.post import PostRepository
from app.database.session import SessionLocal
from app.services.fetch_post import fetch_random_post
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
import random
from app.states.post_states import AddPostState


router = Router()


@router.callback_query(F.data == "create_post")
async def ask_post_title(callback:CallbackQuery, state:FSMContext):
    await state.set_state(AddPostState.waiting_for_post_id)
    await callback.message.answer("Введите номер поста (только цифры):")


    pass