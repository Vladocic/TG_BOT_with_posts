from aiogram.types import CallbackQuery
from aiogram import Router, F
from app.database.session import SessionLocal
from app.repositories.post import PostRepository
from app.services.post_service import get_paginated_posts_text
from app.utils.keyboard_helpers import build_menu_2_buttons
from app.utils.show_text import show_text
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data.startswith("show_more:"))
async def handle_show_more(callback:CallbackQuery, state: FSMContext):
    """
    Обрабатывает нажатие кнопки "Показать ещё" и выводит следующую порцию постов.
    Использует пагинацию: извлекает из callback.data смещение (offset), 
    получает следующие 5 постов из базы данных, выводит их в чат и добавляет кнопку
    для дальнейшего листания (если посты есть).
    :param callback: Объект CallbackQuery от Telegram.
    :param state: Контекст FSM-состояния пользователя.
    """
    await state.clear()
    try:
        offset = int(callback.data.split(":")[1])
    except (IndexError, ValueError):
        await callback.message.answer("❌ Неверный формат запроса")
        return
    async with SessionLocal() as session:
        text, has_more = await get_paginated_posts_text(session, offset)

        if not text:
            await callback.message.answer("⚠️ Больше постов нет")
            return

        buttons = build_menu_2_buttons("📩 Показать ещё", f"show_more:{offset+5}") if has_more else None
    await callback.message.answer(text, reply_markup=buttons)



        text, has_more = await get_paginated_posts_text(session, offset)


        await get_paginated_posts_text(session, offset)
        repo = PostRepository(session)
        posts = await repo.get_posts_paginated(offset=offset)

        if not posts:
            await callback.message.answer("⚠️ Больше постов нет")
            return

        text = show_text(posts)
            
        if len(posts) == 5:
            buttons = build_menu_2_buttons(text="📩 Показать ещё", callback_data=f"show_more:{offset+5}")
        else:
            text ='Это последние посты!\n\n '+text
            buttons = None     

        await callback.message.answer(text,reply_markup= buttons)
            

