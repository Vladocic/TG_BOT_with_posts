from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def build_menu_keyboard(text: str, callback_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text,callback_data)],
        [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
    ])
    
