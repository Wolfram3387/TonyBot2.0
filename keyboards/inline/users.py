from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from typing import List

from keyboards.default import UserButtons


u_cancel_1 = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text=UserButtons.cancel.text, callback_data=UserButtons.cancel.callback)
        ],
    ],
    resize_keyboard=True,
)

u_skip = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text=UserButtons.skip.text, callback_data=UserButtons.skip.callback)
        ],
    ],
    resize_keyboard=True,
)

u_finish_entering = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text=UserButtons.finish_entering.text, callback_data=UserButtons.finish_entering.callback)
        ],
        [
            InlineKeyboardButton(text=UserButtons.cancel_entering.text, callback_data=UserButtons.cancel_entering.callback)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

answer_CD = CallbackData('answers', 'level', 'category', 'title_id')


def make_callback_data(level=0, category=0, title_id=0):
    return answer_CD.new(level=level, category=category, title_id=title_id)


def generate_markup(buttons: List[InlineKeyboardButton], markup: InlineKeyboardMarkup = InlineKeyboardMarkup()):
    """Создаёт клавиатуру с row_width=1 и пролистыванием страниц, если это потребуется"""
    btn_1 = InlineKeyboardButton(text='<-', callback_data=make_callback_data())
    btn_2 = InlineKeyboardButton(text='', callback_data=make_callback_data())
    btn_3 = InlineKeyboardButton(text='->', callback_data=make_callback_data())
    row_number = 1
    for button in buttons:
        if row_number % 10 != 0:
            markup.row(button)
            row_number += 1
        else:
            markup.row()
            row_number = 1
