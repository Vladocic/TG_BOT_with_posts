from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from app.utils.keyboard_helpers import build_menu_back_button

async def is_number(message:Message) -> bool:
    if not message.text.isdigit():
        button = build_menu_back_button()
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])
        await message.answer("❗ Введите число.", reply_markup=button)
        return False
    return True