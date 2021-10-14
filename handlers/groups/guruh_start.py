from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.asosiy import buttons
from loader import dp
from filters import Group


@dp.message_handler(Group(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n")
    await message.answer("siz guruhdan murojat qildingiz")

