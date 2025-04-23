from aiogram.types import CallbackQuery
from pydantic import ValidationError
from app.database.session import SessionLocal
from app.schemas.post import PostSchema
from app.utils.case_converter import camel_to_snake_case
from app.utils.show_text import show_text
from app.repositories.post import PostRepository



async def normalize_and_save_posts(posts: list[dict], session, callback: CallbackQuery) -> str | None:
    async with SessionLocal() as session:

        posts = camel_to_snake_case(posts)
        
        try:
            validated = [PostSchema(**post) for post in posts]
        except ValidationError as e:
            await callback.message.answer(f"❌ Ошибка валидации: {e}")
            return
        
        repo = PostRepository(session)
        await repo.save_many(validated)

        text = show_text(validated)

    

    pass