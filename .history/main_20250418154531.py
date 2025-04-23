from app.bot import bot,dp
from app.handlers import register_handlers



async def main():
    register_handlers(dp)
    print("🚀 Бот запущен в режиме polling...")
    await dp.start_polling(bot)



if __name__=="__name__"