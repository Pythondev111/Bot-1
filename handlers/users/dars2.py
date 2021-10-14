
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold,italic,link

from loader import dp
from  keyboards.default.python_tugmalar import python_buttons

@dp.callback_query_handler(text = '2-dars')
async def bot_start(call:CallbackQuery):

    await call.message.answer(hbold(" dars ")+"2 tugmasi bosildi \n"+
                              "  <a href = 'https://kundalik.com/' > kanalga azo bo'lish </a>" ,reply_markup=python_buttons)
    await call.answer(cache_time=60)
