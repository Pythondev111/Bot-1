from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.default.contact import contact_buttons
from loader import dp
from filters import Group

@dp.message_handler(Group(), CommandHelp())
async def bot_help(message: types.Message):



    await message.answer("guruhdan yordam so'radiz ")
