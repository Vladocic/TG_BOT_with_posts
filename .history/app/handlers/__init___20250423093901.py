from aiogram import Dispatcher
from aiogram.filters import CommandStart
from app.handlers.start import start
from app.handlers.get_all_posts import router as posts_router
from app.handlers.show_more import router as show_more_router
from app.handlers.get_random_post import router as random_router
from app.handlers.back_to_menu import router as back_to_menu_router
from app.handlers.get_post_by_id import router as get_post_id_router
from app.handlers.create_post import router as create_post_router
from app.handlers.delete_all import router as delete_all_router
from app.handlers.delete_post import router as delete_post_router



def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.include_router(posts_router)
    dp.include_router(show_more_router)
    dp.include_router(random_router)
    dp.include_router(back_to_menu_router)
    dp.include_router(get_post_id_router)
    dp.include_router(create_post_router)
    dp.include_router(delete_post_router)
        dp.include_router(delete_post_router)







