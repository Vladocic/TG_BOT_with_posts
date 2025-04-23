from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN


if BOT_TOKEN is None:
    raise ValueError('No Bot_token in files')


bot = Bot(
    token = BOT_TOKEN, 
    default = DefaultBotProperties(parse_mode= ParseMode.HTML) 
)

print(bot)
print(Bo)
dp = Dispatcher()
