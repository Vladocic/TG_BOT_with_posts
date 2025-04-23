from aiogram.types import CallbackQuery
from aiogram import Router, F
from app.handlers.start import start
from aiogram.fsm.context import FSMContext


router = Router()

@router.callback_query(F.data == "back_to_menu")
async def handle_back_to_menu(callback: CallbackQuery,state: FSMContext):
    await state.c
    await start(callback.message)