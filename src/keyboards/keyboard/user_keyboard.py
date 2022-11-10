# модуль содержит обычные клавиатуры

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='X'),
            KeyboardButton(text='0')
        ]
    ],
    resize_keyboard=True
)

another_game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Еще одна игра')
        ]
    ],
    resize_keyboard=True
)

