from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_onatili import onatili_buttons
from loader import dp


@dp.message_handler(text = 'Ona tili')
async def bot_start(message: types.Message):

    await message.answer('Ona tili darsliklariga hush kelibsiz',reply_markup=onatili_buttons)
