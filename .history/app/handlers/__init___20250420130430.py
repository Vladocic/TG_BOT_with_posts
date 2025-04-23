from aiogram import Dispatcher, F, Router
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import router as posts_router
from app.handlers.show_more import router as show_more



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart)
    dp.include_router(posts_router)
    dp.include_router()
