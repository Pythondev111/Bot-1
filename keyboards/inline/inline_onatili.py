from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

onatili_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='😁',callback_data='onatili_darslari'),
            InlineKeyboardButton(text="2-dars",callback_data= '2-dars'),

        ],
        [
            InlineKeyboardButton(text=""" 🤔 """,switch_inline_query=" Zo'r bot ekan "),
            InlineKeyboardButton(text="Kanalga azo bo'lish",url='https://t.me/UstozShogird'),

        ],


    ],
    resize_keyboard = True
)

onatili_dars1_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-dars',callback_data='dars1'),
            InlineKeyboardButton(text="2-dars",callback_data= 'dars2'),

        ],


    ],
    resize_keyboard = True
)

