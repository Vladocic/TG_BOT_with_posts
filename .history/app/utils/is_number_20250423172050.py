from aiogram.types import Message
from app.utils import build_menu_back_button

async def is_number(message:Message) -> bool:
    """
    Проверяет, является ли текст сообщения числом. 
    Если нет — отправляет предупреждение с кнопкой возврата в меню.
    :param message: Объект сообщения от пользователя.
    :return: True, если сообщение содержит только цифры, иначе False.
    """
    if not message.text.isdigit():
        button = build_menu_back_button()
        await message.answer("❗ Введите число.", reply_markup=button)
        return False
    return True