from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
    )


menu = [
    [
        InlineKeyboardButton(
            text='📝 Указать препарат',
            callback_data='generate_text'
        ),
        InlineKeyboardButton(
            text='🖼 Создать расписание приема лекарств',
            callback_data='generate_text'
        )
    ],
    [
        InlineKeyboardButton(
            text='🔎 Помощь',
            callback_data='help'
        )
    ]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='◀️ Выйти в меню')
        ]
    ], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='◀️ Выйти в меню', callback_data='menu')
        ]
    ]
)
