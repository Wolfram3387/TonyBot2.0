import logging
from aiogram import Dispatcher

from data.config import ADMINS
from keyboards.default import a_menu


async def on_startup_notify(dp: Dispatcher):
    for admin_id in ADMINS:
        try:
            await dp.bot.send_message(admin_id, "Бот запущен", reply_markup=a_menu)

        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    for admin_id in ADMINS:
        try:
            await dp.bot.send_message(admin_id, "Бот остановлен!")

        except Exception as err:
            logging.exception(err)
