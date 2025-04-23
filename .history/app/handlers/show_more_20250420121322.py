from aiogram.types import CallbackQuery, F
from aiogram import Router, F
from app.database.session import SessionLocal


router = Router()


@router.callback_query(F.data == "show_more", session = )
async def handle_show_more(callback:CallbackQuery):

