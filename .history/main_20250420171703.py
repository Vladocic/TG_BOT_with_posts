import asyncio
from app.states import post_states  # чтобы FSM-класс подгрузился
from app.bot import bot, dp
from app.handlers import register_handlers
from app.commands.commands import set_commands


async def main():

    register_handlers(dp)
    await set_commands(bot)
    print("🚀 Бот запущен в режиме polling...")
    await dp.start_polling(bot)



if __name__=="__main__":
    asyncio.run(main())
