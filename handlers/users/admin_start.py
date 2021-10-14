from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.asosiy import buttons
from loader import dp
from filters import Admin


@dp.message_handler(Admin(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom Admin botga hush kelibsiz, {message.from_user.full_name}!\n")
