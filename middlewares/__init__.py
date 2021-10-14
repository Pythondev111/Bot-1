from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .checking import Asosiy


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Asosiy())
