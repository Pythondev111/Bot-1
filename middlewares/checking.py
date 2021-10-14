import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import Kanallar
from keyboards.default.asosiy import buttons
from utils.misc import azo_bolish
from loader import bot


class Asosiy(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            logging.info(user)
        elif update.callback_query:
            user = update.callback_query.from_user.id

        else:
            return


        final_status = True
        for channel in Kanallar:
            status = await azo_bolish.azolik(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                button = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text=f"{channel.title}\n",url=invite_link)
                        ]

                    ]
                )

                await update.message.answer(text="Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling",reply_markup=button)

        if not final_status:
            await update.message.answer(text='.', disable_web_page_preview=True)

            raise CancelHandler()
