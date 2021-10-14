from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold,italic,link
from  keyboards.default.python_tugmalar import python_buttons
from keyboards.inline.inline_onatili import onatili_dars1_buttons
from loader import dp


@dp.callback_query_handler(text = 'onatili_darslari')
async def bot_start(call:CallbackQuery):

    await call.message.answer( hbold(" 1- darsga hush kelibsiz\n ") +
                              """ Mayami universitetida bakalavr dasturlarida o'qish uchun Stamps stipendiyasiga arizalar ochiq.  Xalqaro talabalardan arizalar qabul qilinadi. Grant olish uchun talaba universitet tomonidan taqdim etilgan ta'lim yo'nalishlaridan biriga hujjat topshirishi kerak.

Grant to'liq o'qish to'lovlarini, kampusda yashash, tibbiy sug'urta, ovqatlanish va boshqalarni o'z ichiga oladi.<a href = 'https://t.me/grantlar_stipendiyalar_1' >Talaba </>  har bir kuz va bahor semestrlarida kamida 12 kredit soatiga ega bo'lgan to'liq bakalavr dasturini tamomlashi kerak, bu o'quv yili uchun kamida 24 kredit soatini tashkil qiladi va o'quv yili davomida GPA kamida 3.0 bo'lishi kerak. . """,)
    await call.answer(cache_time=60)
