import asyncio
from app.bot import bot,dp
from app.handlers import register_handlers
from app.commands import set_commands



async def main():

    register_handlers(dp)
    await set_commands()
    print("🚀 Бот запущен в режиме polling...")
    await dp.start_polling(bot)



if __name__=="__main__":
    asyncio.run(main())
