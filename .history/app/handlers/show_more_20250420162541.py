from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F
from app.database.session import SessionLocal
from app.repositories.post import PostRepository
from app.utils.show_text import show_text


router = Router()


@router.callback_query(F.data.startswith("show_more:"))
async def handle_show_more(callback:CallbackQuery):
        async with SessionLocal() as session:
            try:
                offset = int(callback.data.split(":")[1])
            except (IndexError, ValueError):
                await callback.message.answer("❌ Неверный формат запроса")
                return
    
            repo = PostRepository(session)
            posts = await repo.get_posts_paginated(offset=offset)

            if not posts:
                await callback.message.answer("⚠️ Больше постов нет")
                return

            text = show_text(posts)
            
            
            if len(posts) == 5:
                 buttons = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="📩 Показать ещё", callback_data=f"show_more:{offset+5}")],
                    [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
                ])
            else:
                text ='Это последние посты!\n\n '+text
                button = None     

            await callback.message.answer(text,reply_markup= button)
            

