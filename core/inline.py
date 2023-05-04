from aiogram.types import *

auth_inline = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text="Места", callback_data="menu_1"),
    InlineKeyboardButton(text="Дата" , callback_data="menu_2"),
    InlineKeyboardButton(text="Адрес", callback_data="menu_3"),
    InlineKeyboardButton(text="Поиск...", switch_inline_query_current_chat=""),
)

location_inline = InlineKeyboardMarkup(row_width=1)
data_inline = InlineKeyboardMarkup()
adress_inline = InlineKeyboardMarkup(row_width=2)