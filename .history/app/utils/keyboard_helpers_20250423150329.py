from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def build_menu_2_buttons(text: str, callback_data: str) -> InlineKeyboardMarkup:
    """
    Создаёт клавиатуру с двумя кнопками:
    1. Пользовательская кнопка с заданным текстом и callback_data.
    2. Кнопка возврата в главное меню.
    :param text: Текст для пользовательской кнопки.
    :param callback_data: Callback-данные для пользовательской кнопки.
    :return: Объект клавиатуры InlineKeyboardMarkup.
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text,callback_data=callback_data)],
        [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
    ])
    

def build_menu_back_button()->InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
    ])