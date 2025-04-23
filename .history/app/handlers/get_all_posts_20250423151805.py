from aiogram.types import CallbackQuery
from aiogram import Router, F
from app.services.fetch_post import fetch_all_posts
from app.utils.keyboard_helpers import build_menu_2_buttons
from app.utils.post_helpers import normalize_and_save_posts
from app.database.session import SessionLocal
from aiogram.fsm.context import FSMContext


router = Router()


@router.callback_query(F.data == "get_all_posts")
async def handle_get_all_posts(callback:CallbackQuery, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "📚 Все посты".

    Загружает все посты с внешнего API, преобразует и валидирует данные,
    сохраняет в базу данных, очищает предыдущее состояние и отправляет
    пользователю первые 5 постов с кнопкой "Показать ещё".

    :param callback: Объект CallbackQuery от Telegram.
    :param state: Объект FSMContext для работы с состояниями.
    """
    await state.clear() 
    async with SessionLocal() as session:

            posts = await fetch_all_posts()
            result = await normalize_and_save_posts(posts, session, callback)
            text = result["preview"]
            buttons = build_menu_2_buttons(text="📩 Показать ещё", callback_data="show_more:5")
            await callback.message.answer(text,reply_markup = buttons)


