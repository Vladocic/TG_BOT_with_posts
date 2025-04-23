from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router
from pydantic import ValidationError
from app.services.fetch_post import fetch_all_posts
from app.utils.case_converter import camel_to_snake_case
from app.schemas.post import PostSchema
from app.repositories.post import PostRepository
from sqlalchemy.ext.asyncio import AsyncSession
from

router = Router()



@router.callback_query
async def handle_get_all_posts(callback:CallbackQuery, session: AsyncSession): 
        print(f'-------\n{callback.model_dump()}')
        posts = await fetch_all_posts()
        posts = camel_to_snake_case(posts)
        try:
            validated = [PostSchema(**post) for post in posts]
        except ValidationError as e:
            await callback.message.answer(f"❌ Ошибка валидации: {e}")
            return
        
        repo = PostRepository(session)

        await repo.save_many(validated)

        preview = validated[:5]
        text = '\n\n'.join(f'<b>{post.title}</b>\n{post.body}' for post in preview )


        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📩 Показать ещё", callback_data="show_more")]
        ])
        await callback.message.answer(
            text,
            reply_markup = button
        )


