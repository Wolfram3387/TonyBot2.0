from aiogram import types

from keyboards.inline.users import answer_CD, _categories, generate_markup
from handlers.users.commands import show_user_menu
from loader import dp


async def show_main_menu(callback: types.CallbackQuery, **kwargs):
    await show_user_menu(message=callback.message, state=dp.current_state(user_id=callback.from_user.id))


async def list_categories(callback: types.CallbackQuery, level, **kwargs):
    categories = [...]  # TODO Выбрать все категории вариантов из БД
    markup = await generate_markup(buttons=categories)
    text = '...'
    await callback.message.edit_text(text=text, reply_markup=markup)


async def list_titles(callback: types.CallbackQuery, level, category, **kwargs):
    pass


async def list_take_answers(callback: types.CallbackQuery, level, category, title_id):
    pass


@dp.callback_query_handler(answer_CD.filter())
async def navigate(callback: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    title_id = callback_data.get('title_id')

    levels = {
        '0': show_main_menu,
        '1': list_categories,
        '2': list_titles,
        '3': list_take_answers,
    }

    current_level_function = levels[current_level]
    await current_level_function(callback=callback, level=current_level, category=category, title_id=title_id)
