from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.python_tugmalar import python_buttons
from loader import dp


@dp.message_handler(text = 'Matematika')
async def bot_start(message: types.Message):

    await message.answer('Python darsliklariga hush kelibsiz',reply_markup=python_buttons )
