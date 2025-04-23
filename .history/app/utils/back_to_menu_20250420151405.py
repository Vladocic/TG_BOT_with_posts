from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def back_to_menu_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ]
    )