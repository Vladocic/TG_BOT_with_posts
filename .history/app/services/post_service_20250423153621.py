from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.repositories.post import PostRepository
from app.utils.show_text import show_text


def build_main_menu() -> InlineKeyboardMarkup:
    """
    Создаёт главное меню с кнопками управления постами.
    :return: InlineKeyboardMarkup с кнопками действий.
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📚 Все посты", callback_data="get_all_posts")],
            [InlineKeyboardButton(text="🎲 Случайный пост", callback_data="get_random_post")],
            [InlineKeyboardButton(text="🔢 Пост по номеру", callback_data="get_post_by_id")],
            [
                InlineKeyboardButton(text="➕ Добавить 📝", callback_data="create_post"),
                InlineKeyboardButton(text="🗑 Удалить ❌", callback_data="delete_post_by_id")
            ],
            [InlineKeyboardButton(text="💣 Удалить всё (необратимо)", callback_data="delete_all")]
        ]
    )


async def get_paginated_posts_text(session, offset: int = 0) -> tuple[str, bool]:
    """
    Получает посты с пагинацией и возвращает текст + флаг, есть ли ещё посты.
    :param session: Сессия базы данных.
    :param offset: Смещение.
    :return: (text, has_more)
    """
    repo = PostRepository(session)
    posts = await repo.get_posts_paginated(offset=offset)
    text = show_text(posts)
    has_more = len(posts) == 5
    return text, has_more