from aiogram import Dispatcher
from aiogram.filters import CommandStart

from .start import start

from .get_all_posts import router as posts_router
from .show_more import router as show_more_router
from .get_random_post import router as random_router
from .get_post_by_id import router as get_post_id_router
from .create_post import router as create_post_router
from .delete_post import router as delete_post_router
from .delete_all import router as delete_all_router
from .back_to_menu import router as back_to_menu_router


def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())

    routers = [
        posts_router,
        show_more_router,
        random_router,
        get_post_id_router,
        create_post_router,
        delete_post_router,
        delete_all_router,
        back_to_menu_router
    ]

    routers = [

    ]
    dp.include_router(posts_router)
    dp.include_router(show_more_router)
    dp.include_router(random_router)
    dp.include_router(back_to_menu_router)
    dp.include_router(get_post_id_router)
    dp.include_router(create_post_router)
    dp.include_router(delete_post_router)
    dp.include_router(delete_all_router)







