from aiogram import Dispatcher
from aiogram.filters import CommandStart
from app.handlers.start import start


def register_handlers(dp: Dispatcher):
