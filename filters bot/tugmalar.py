from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bosh_menu_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Ota-onalar uchun", callback_data="1"),
            InlineKeyboardButton(text="O'quvchi uchun", callback_data="2"),
        ],
        [
            InlineKeyboardButton(text="Mehmon uchun", callback_data="3"),
        ]  
    ]
)