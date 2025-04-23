from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

async def is_number(message:Message):
    if not message.text.isdigit():
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])
        await message.answer("❗ Введите число.", reply_markup=button)
        return