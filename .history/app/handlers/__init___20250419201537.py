from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import handle_get_all_posts
from app.database.session import get_session
from aiogram.utils import dependency as di
from aiogram.utils.di import Depends



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart)
    dp.callback_query.register(handle_get_all_posts, F.data == 'get_all_posts', get_session)
