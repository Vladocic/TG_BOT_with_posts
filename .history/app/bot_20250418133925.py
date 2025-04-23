from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from os import getenv


TOKEN = getenv("BOT_TOKEN")

bot = Bot(
    token = TOKEN, default = DefaultBotProperties(parse_mode= ParseMode.HTML)  )

dp = Dispatcher()
