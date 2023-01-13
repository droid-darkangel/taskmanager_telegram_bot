from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():

    kb = [
        [
            KeyboardButton(text='💻 Помощь')
        ],
        [
            KeyboardButton(text='✅ добавить')
        ],
        [
            KeyboardButton(text='❌ удалить')
        ],
        [
            KeyboardButton(text='🎲 рандом')
        ],
        [
            KeyboardButton(text='👀 показать')
        ]
    ]

    menu = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return menu