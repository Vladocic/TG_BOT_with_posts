from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN
from os import getenv


TOKEN = getenv("BOT_TOKEN")
print(TOKEN)
if TOKEN is None:
    raise ValueError('No Bot_token in files')

bot = Bot(
    token = TOKEN, 
    default = DefaultBotProperties(parse_mode= ParseMode.HTML) 
)

dp = Dispatcher()
