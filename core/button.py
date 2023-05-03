from aiogram.types import *


reg_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Зарегистрироваться", request_contact=True)
)

auth_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Категории"),
    KeyboardButton(text="Дата"),
    KeyboardButton(text="Места"),
    KeyboardButton(text="Адрес"),
    KeyboardButton(text="О Нас"),
)
category_db = ReplyKeyboardMarkup(resize_keyboard=True)
# calendar_db = ReplyKeyboardMarkup(resize_keyboard=True)
location_db = ReplyKeyboardMarkup(resize_keyboard=True)

next_back_db = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text=">>>"),
    KeyboardButton(text="<<<"),
    KeyboardButton(text="Меню"),
)