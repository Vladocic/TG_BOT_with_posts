from aiogram.types import TelegramObject
from pydantic import ValidationError
from app.schemas.post import PostSchema
from app.utils.case_converter import camel_to_snake_case
from app.utils.show_text import show_text
from app.repositories.post import PostRepository



async def normalize_and_save_posts(posts: list[dict], session, sender: TelegramObject) -> dict:
    """
    Преобразует список словарей с camelCase в snake_case, валидирует данные через Pydantic,
    сохраняет в базу данных и возвращает текстовое представление постов.

    :param posts: Список постов в формате словарей (из внешнего API).
    :param session: SQLAlchemy-сессия для работы с базой данных.
    :param sender: Объект Telegram (Message или CallbackQuery) для отправки ошибок.
    :return: Словарь с двумя ключами:
        - "all": строка с форматированным выводом всех постов,
        - "preview": строка с первыми 5 постами.
    """
    posts = camel_to_snake_case(posts)
        
    try:
        validated = [PostSchema(**post) for post in posts]
    except ValidationError as e:
        await sender.message.answer(f"❌ Ошибка валидации: {e}")
        return
        
    repo = PostRepository(session)
    await repo.save_many(validated)

    return {
        "all": show_text(validated),
            "preview": show_text(validated[:5])
        }
    