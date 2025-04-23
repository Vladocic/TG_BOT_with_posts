from _asynci

async def is_numer(message:Mes)
    if not message.text.isdigit():
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🏠 В меню", callback_data="back_to_menu")]
        ])
        await message.answer("❗ Введите число.", reply_markup=button)
        return