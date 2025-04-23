from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import handle_get_all_posts



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart)
    dp.callback_query.register(handle_get_all_posts, f. )