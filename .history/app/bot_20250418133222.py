import asyncio
from aiogram import Bot, Dispatcher
from os import getenv


TOKEN = getenv("BOT_TOKEN", parse_mode = Ht)

bot = Bot()

dp = Dispatcher()
