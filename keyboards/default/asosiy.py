from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Matematika',),
            KeyboardButton(text="Ona tili",),

        ],
        [
            KeyboardButton(text="Eng"),
            KeyboardButton(text="Rus"),
        ],

    ],
    resize_keyboard = True
)
