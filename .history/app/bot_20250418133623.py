import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from os import getenv


TOKEN = getenv("BOT_TOKEN", parse_mode = Ht)

bot = Bot(token = TOKEN, default = DefaultBotProperties(parse_mode= ParseMode.H)  )

dp = Dispatcher()
