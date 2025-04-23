from aiogram.types import CallbackQuery
from aiogram import Router, F
from app.services.post_service import load_all_posts_preview
from app.utils import build_menu_2_buttons
from app.database.session import SessionLocal
from aiogram.fsm.context import FSMContext


router = Router()


@router.callback_query(F.data == "get_all_posts")
async def handle_get_all_posts(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает кнопку "📚 Все посты", загружает посты из API, сохраняет в БД и показывает первые 5.
    """
    await state.clear() 
    async with SessionLocal() as session:
        text = await load_all_posts_preview(session, callback)
        buttons = build_menu_2_buttons(text="📩 Показать ещё", callback_data="show_more:5")
        await callback.message.answer(text, reply_markup=buttons)

