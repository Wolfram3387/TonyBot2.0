from aiogram import types
from filters import IsPrivate, IsAdmin
from aiogram.dispatcher import FSMContext
from loader import dp, users_db
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart

from keyboards.default import a_menu
from keyboards.default import AdminButtons


@dp.message_handler(CommandHelp(), IsPrivate(), IsAdmin(), state='*')
async def help_for_admin(message: types.Message):
    """Команда /help для админа"""
    text = [
        'Список команд для админа: ',
        '/menu - Показать меню',
        '/state - Проверить состояние',
        '/users - Показать id пользователей',
        '/variants - Показать id вариантов',
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(CommandStart(), IsPrivate(), IsAdmin(), state='*')
async def start_for_admin(message: types.Message):
    """Команда /start для админа"""
    await message.answer('Зачем админу команда старт?...')


@dp.message_handler(Command('menu'), IsPrivate(), IsAdmin(), state='*')
async def show_admin_menu(message: types.Message, state: FSMContext):
    """Показывает раскладку меню для админа"""
    await state.finish()
    await message.answer(AdminButtons.menu, reply_markup=a_menu)


@dp.message_handler(Command('users'), IsPrivate(), IsAdmin(), state='*')
async def show_users(message: types.Message):
    """Показывает всех пользователей и их id для админа"""
    users = '\n'.join(['{0:>12} - {1:<}'.format(line[0], line[1]) for line in sorted(
        users_db.select_all_users(), key=lambda line: line[1])])
    await message.answer(f'Текущие пользователи:\n{users}')
