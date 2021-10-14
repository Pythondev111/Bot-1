import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.asosiy import buttons
from loader import dp, db, bot
from filters import Shaxsiy

@dp.message_handler( CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    id = message.from_user.id
    fam = message.from_user.last_name
    try:
        db.add_user(id,ism)
    except Exception as s:
        print(s)

    await message.answer('Fanlardan birini tanlang ',reply_markup=buttons )
# import logging
#
# from aiogram import types
# from data.config import Kanallar
# from keyboards.inline.check import button
# from loader import bot, dp
# from utils.misc import azo_bolish
# from keyboards.inline.check import button
#
# @dp.message_handler(commands=['start'])
# async def show_channels(message: types.Message):
#     channels_format = str()
#     for channel in Kanallar:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#         # logging.info(invite_link)
#         channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
#
#     await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
#                          f"{channels_format}",
#                          reply_markup=button,
#                          disable_web_page_preview=True)
#
#
# @dp.callback_query_handler(text="check")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in Kanallar:
#         status = await azo_bolish.azolik(user_id=call.from_user.id,
#                                           channel=channel)
#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
#                        f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
#
#     await call.message.answer(result, disable_web_page_preview=True)