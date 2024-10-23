from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, keyboard_button, ReplyKeyboardMarkup, ReplyKeyboardRemove

text = [
    [KeyboardButton(text='Нагрубить'),
    KeyboardButton(text='Извиниться'),
    KeyboardButton(text='Узнать ID')]
]

menu = ReplyKeyboardMarkup(keyboard=text)