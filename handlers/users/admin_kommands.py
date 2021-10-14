import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state

from states.holatlar import NewPost

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()

    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):

    await message.answer(text='reklama yuboring' )
    await NewPost.Reklama.set()

@dp.message_handler( state=NewPost.Reklama)
async def gets(message: types.Message,state:FSMContext):
    await state.update_data(text=message.text, mention=message.from_user.get_mention())
    await NewPost.next()
    async with state.proxy() as data:
        text = data.get("text")




    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=f"{text} yuborildi")
        await asyncio.sleep(0.05)
    await state.finish()

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")