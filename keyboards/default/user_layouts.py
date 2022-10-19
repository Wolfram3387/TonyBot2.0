from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from collections import namedtuple


class UserButtons:
    Button = namedtuple('Button', 'text callback')

    menu = Button('Меню 📒', 'menu')
    cancel = Button('Отменить', 'cancel')
    back = Button('Назад', 'back')
    finish_entering = Button('Завершить ввод', 'finish_entering')
    cancel_entering = Button('Отменить ввод', 'cancel_entering')
    skip = Button('Пропустить', 'skip')
    send_answers = Button('Отправить ответы 📩', 'send_answers')
    variants = Button('Варианты 🗂', 'variants')


u_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(UserButtons.send_answers.text)
        ]
    ],
    resize_keyboard=True,
)
