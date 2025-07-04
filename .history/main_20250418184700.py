import asyncio
from app.bot import bot,dp
from app.handlers import register_handlers
from app.services.fetch_post import fetch_all_posts



async def main():
    data = await fetch_all_posts()


    register_handlers(dp)
    print("🚀 Бот запущен в режиме polling...")
    await dp.start_polling(bot)



if __name__=="__main__":
    asyncio.run(main())
