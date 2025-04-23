from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart


async def dd (messgae: types.Message):
    InlineKeyboardMarkup([InlineKeyboardButton()])