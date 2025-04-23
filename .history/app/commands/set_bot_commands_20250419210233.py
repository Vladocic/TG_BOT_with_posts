from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="get", description="Все посты"),
        BotCommand(command="random", description="Случайный пост"),
        BotCommand(command="add", description="Добавить пост"),
        BotCommand(command="delete", description="Удалить пост"),
    ]
    await bot.set_my_commands(commands)