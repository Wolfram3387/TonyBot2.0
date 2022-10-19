from aiogram import types
from utils.misc import rate_limit
from filters import IsPrivate, IsUser
from sqlalchemy.exc import IntegrityError
from aiogram.dispatcher import FSMContext
from loader import dp, users_db
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import u_menu
from keyboards.default import UserButtons
from utils.texts import COMMAND_START


@dp.message_handler(CommandStart(), IsUser(), IsPrivate(), state='*')
async def start_for_user(message: types.Message, state: FSMContext):
    """Команда /start для пользователя"""
    try:
        users_db.add_user(
            user_id=message.from_user.id,
            name=message.from_user.full_name
        )
        await message.answer(COMMAND_START.format(name=message.from_user.full_name), reply_markup=u_menu)
    except IntegrityError:
        await state.finish()
        await message.answer('Бот перезапущен', reply_markup=u_menu)


@dp.message_handler(Command('menu'), IsUser(), IsPrivate(), state='*')
async def show_user_menu(message: types.Message, state: FSMContext):
    """Показывает раскладку меню для пользователя"""
    await state.finish()
    await message.answer(UserButtons.menu, reply_markup=u_menu)
