from aiogram import Dispatcher
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import router as posts_router
from app.handlers.show_more import router as show_more_router
from app.handlers.get_random_post import router as random_router



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart)
    dp.include_router(show_more_router,show_more_router,random_router)
    dp.include_router(show_more_router,show_more_router,random_router)
    dp.include_router(show_more_router,show_more_router,random_router)


