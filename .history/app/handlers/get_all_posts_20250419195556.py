from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pydantic import ValidationError
from app.services.fetch_post import fetch_all_posts
from app.utils.case_converter import camel_to_snake_case
from app.schemas.post import PostSchema
from app.repositories.post import PostRepository


async def handle_get_all_posts(callback:CallbackQuery):
        print(f'-------\n{callback.model_dump()}')
        posts = await fetch_all_posts()
        posts = camel_to_snake_case(posts)
        try:
            validated = [PostSchema(**post) for post in posts]
        except ValidationError as e:
            await callback.message.answer(f"❌ Ошибка валидации: {e}")
            return
        
        repo = PostRepository()
        
        PostRepository.save_many(validated)



        five_posts = posts[0:5]
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📩 Показать ещё", callback_data="show_more")]
        ])
        await callback.message.answer(
            f"первые 5 постов: {five_posts}",
            reply_markup = button
        )


