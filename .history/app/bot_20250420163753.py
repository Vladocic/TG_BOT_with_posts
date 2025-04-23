from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN


bot = Bot(
    token = BOT_TOKEN, 
    default = DefaultBotProperties(parse_mode= ParseMode.HTML) 
)


dp = Dispatcher(storage=Memo)
