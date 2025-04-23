from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from app.models.post import Post
from app.repositories.post import PostRepository
from app.states.post_states import AddPostState
from app.database.session import SessionLocal

router = Router()


@router.callback_query(F.data == "delete_all")
async def delete_all_posts(callback:CallbackQuery):
    async with SessionLocal() as session:
        repo = PostRepository(session)
        result = await repo.del_all_posts()

        text = 'Все данные удалены' if result else 
        if not result:
            text = 'Все данные удалены'

    pass