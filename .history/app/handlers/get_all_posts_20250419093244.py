from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from app.services.fetch_post import fetch_all_posts


async def handle_get_all_posts(callback:CallbackQuery):
        print(f'{callback)
        posts = await fetch_all_posts()
        five_posts = posts[0:5]
        button = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📩 Показать ещё", callback_data="show_more")]
        ])

        await callback.message.answer(
            f"первые 5 постов: {five_posts}",
            reply_markup = button
        )


