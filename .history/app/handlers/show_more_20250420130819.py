from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F
from app.database.session import SessionLocal
from app.repositories.post import PostRepository
from app.utils.show_text import show_text
from app.models.post import Post


router = Router()


@router.callback_query(F.data.startswith("show_more:"))
async def handle_show_more(callback:CallbackQuery):
        async with SessionLocal() as session:
            offset = int(callback.data.split(":")[1])

            repo = PostRepository(session)
            posts = await repo.get_posts_paginated(offset=offset)

            if not posts:
                await callback.message.answer("⚠️ Больше постов нет")
                return

            text = show_text(posts)
            
            
            if len(posts) == 5:
                 button = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="📩 Показать ещё", callback_data=f"show_more:{offset+5}")]
                ])
            else:
                text ='Это последние посты!\n\n '+text
                button = None     

            await callback.message.answer(text,reply_markup= button)
            

