from aiogram import Dispatcher, F, Depends
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import handle_get_all_posts
from app.database.session import get_session



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart)
    dp.callback_query.register(handle_get_all_posts, F.data == 'get_all_posts', Depends(get_session))
