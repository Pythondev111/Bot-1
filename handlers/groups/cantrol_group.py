import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import Group,Admin
from  loader import dp,bot


@dp.message_handler(Group(),Command("o'qish",prefixes="$/"),Admin())
async def faqat_oqish_uchun(message:types.Message):
    azo = message.reply_to_message.from_user
    azo_id = azo.id
    blok = re.compile(r"($o'qish|/o'qish) ?(\d+)? ?([\w+\D]+)?" )
    bloked = blok.match(message.text)
    vaqti = bloked.group(2)
    sababi = bloked.group(3)

    if not vaqti:
        vaqti = 5
    vaqti = int(vaqti)

    bloklanish_vaqti = datetime.datetime.now() + datetime.timedelta(minutes=vaqti)

    await message.chat.restrict(user_id=azo_id,can_send_messages=False,until_date=bloklanish_vaqti)
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.username} {vaqti} minutga bloklandi \n Sababi :{sababi}")

    await asyncio.sleep(5)
    await message.delete()
