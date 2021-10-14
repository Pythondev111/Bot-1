import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from keyboards.default.contact import contact_buttons
from loader import dp,db,bot
from filters import Shaxsiy,Admin

@dp.message_handler( Shaxsiy(),CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
    await message.answer("Location bilan Contactni kiriting ",reply_markup=contact_buttons)
