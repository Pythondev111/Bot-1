from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
python_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-dars'),
            KeyboardButton(text="2-dars"),

        ],
        [
            KeyboardButton(text='3-dars'),
            KeyboardButton(text="4-dars"),

        ],


    ],
    resize_keyboard = True
)
