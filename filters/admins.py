from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class Admin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        azo = await message.chat.get_member(message.from_user.id)
        return azo.is_chat_admin()