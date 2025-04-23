from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.models.post import Post
from app.repositories.post import PostRepository
from app.states.post_states import AddPostState
from app.database.session import SessionLocal


router = Router()

@router.callback_query(F.data == "delete_post_by_id")
async def handle_delete_post(callback: CallbackQuery ,state: FSMContext):
    

