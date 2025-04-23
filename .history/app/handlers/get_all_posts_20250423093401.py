from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F
from app.services.fetch_post import fetch_all_posts
from app.utils.keyboard_helpers import build_menu_2_buttons
from app.utils.post_helpers import normalize_and_save_posts
from app.database.session import SessionLocal
from aiogram.fsm.context import FSMContext


router = Router()


@router.callback_query(F.data == "get_all_posts")
async def handle_get_all_posts(callback:CallbackQuery, state: FSMContext):
        await state.clear() 
        async with SessionLocal() as session:

            posts = await fetch_all_posts()

            result = await normalize_and_save_posts(posts, session, callback)

            text = result["preview"]
        

            buttons = build_menu_2_buttons()
            InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📩 Показать ещё", callback_data="show_more:5")],
                [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
            ])
            await callback.message.answer(text,reply_markup = buttons)


