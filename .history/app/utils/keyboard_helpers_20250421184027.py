from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def build_menu_keyboard(text: str, callback_data: str) -> InlineKeyboardMarkup:
    InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text,callback_data)],
        []


    ])
    pass
