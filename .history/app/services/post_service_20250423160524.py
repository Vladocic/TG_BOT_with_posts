from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.repositories.post import PostRepository
from app.utils.post_helpers import normalize_and_save_posts
from app.utils.show_text import show_text
from app.models.post import Post
from app.services.fetch_post import fetch_random_post, fetch_post_id, fetch_all_posts
from aiogram.types import TelegramObject


import random

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


async def get_random_post_text(session, sender) -> str:
    """
    Возвращает текст случайного поста из БД, если в ней больше 5 записей.
    Иначе — получаем случайный пост из API, сохраняем и возвращаем текст.
    :param session: Сессия SQLAlchemy.
    :param sender: Объект для отправки ошибок (CallbackQuery или Message).
    :return: Готовый текст поста.
    """
    repo = PostRepository(session)
    ids = await repo.get_all_posts_id()

    if len(ids) > 5:
        random_id = random.choice(ids)
        post = await repo.get_post_by_id(random_id)
        return show_text(post)
    else:
        api_post = await fetch_random_post()
        result = await normalize_and_save_posts([api_post], session, sender)
        return result["all"]
    

async def get_post_by_id_text(post_id: int, session, sender: TelegramObject) -> tuple[str, bool]:
    """
    Получает пост по ID: сначала из БД, если нет — из API. 
    Возвращает текст и флаг успешности.

    :param post_id: ID поста
    :param session: Сессия SQLAlchemy
    :param sender: Telegram объект (Message или Callback)
    :return: (текст поста, найден ли пост)
    """
    repo = PostRepository(session)
    post_bd = await repo.get_post_by_id(post_id)

    if post_bd:
        return show_text(post_bd), True

    post = await fetch_post_id(post_id)
    if not post:
        return "", False

    result = await normalize_and_save_posts([post], session, sender)
    return result["all"], True


async def load_all_posts_preview(session, sender: TelegramObject) -> str:
    """
    Загружает все посты из внешнего API, нормализует, сохраняет и возвращает первые 5 постов.

    :param session: Сессия SQLAlchemy
    :param sender: Объект Telegram (CallbackQuery или Message)
    :return: Строка с текстом первых 5 постов
    """
    posts = await fetch_all_posts()
    result = await normalize_and_save_posts(posts, session, sender)
    return result["preview"]

async def delete_post_by_id_service(post_id: int, session) -> bool:
    """
    Удаляет пост из базы данных и Google Sheets по заданному ID.

    :param post_id: ID поста для удаления.
    :param session: Сессия SQLAlchemy.
    :return: True, если пост был удалён, иначе False.
    """
    repo = PostRepository(session)
    return await repo.del_post_by_id(post_id)


async def delete_all_posts_service(session) -> bool:
    """
    Удаляет все посты из базы данных и Google Sheets.

    :param session: Сессия SQLAlchemy.
    :return: True, если хотя бы одна запись была удалена, иначе False.
    """
    repo = PostRepository(session)
    return await repo.del_all_posts()


async def create_post_service(session, user_id: int, title: str, body: str) -> int | None:
    """
    Сохраняет новый пост в базу данных и в Google Таблицу.

    :param session: Сессия SQLAlchemy.
    :param user_id: ID пользователя из Telegram.
    :param title: Заголовок поста.
    :param body: Содержимое поста.
    :return: ID созданного поста или None при ошибке.
    """
    repo = PostRepository(session)
    post = Post(user_id=user_id, title=title, body=body)
    return await repo.save_one(post)