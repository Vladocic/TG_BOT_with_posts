from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from os import getenv


TOKEN = getenv("BOT_TOKEN")

if 

bot = Bot(
    token = TOKEN, 
    default = DefaultBotProperties(parse_mode= ParseMode.HTML) 
)

dp = Dispatcher()
