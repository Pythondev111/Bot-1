from aiogram import types
from filters import Shaxsiy
from loader import dp


# Echo bot
@dp.message_handler( Shaxsiy(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
