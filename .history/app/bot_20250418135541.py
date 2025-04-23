from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN


TOKEN = getenv("BOT_TOKEN")
print(TOKEN)
if TOKEN is None:
    raise ValueError('No Bot_token in files')

bot = Bot(
    token = BOT_TOKEN, 
    default = DefaultBotProperties(parse_mode= ParseMode.HTML) 
)

dp = Dispatcher()
