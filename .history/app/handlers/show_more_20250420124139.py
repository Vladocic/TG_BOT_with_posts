from aiogram.types import CallbackQuery, F, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F
from app.repositories.post import PostRepository

router = Router()


@router.callback_query(F.data.startswith("show_more:"))
async def handle_show_more(callback:CallbackQuery):
        offset = int(callback.data.split(":")[1])
        repo = 
        posts = PostRepository.get_posts_paginated(offset=offset)
        text = '\n\n'.join(
                f'<b>Post #{post.id}\nTitle</b>: {post.title}\n<b>Text</b>: {post.body}'
                for post in posts
            )
        
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📩 Показать ещё", callback_data=f"show_more:{offset+5}")]
        ])

        await callback.message.answer(
            text,
            reply_markup= button

        )
        

