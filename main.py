import random
from os import system
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *

# Created module - Созданный модуль
from core.config import *
from database.dbusers import check_users, registrstion_users, search_inline_mode
from core.button import *

system("clear")
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    user_id = message.chat.id

    check = check_users(user_id)
    if check is None:
        await message.reply("Вы не зарегистрированы", reply_markup=reg_markup)
    else:
        await message.reply(
        "Вы уже у нас зарегистрированы, пользуйтесь на здоровье 😇", reply_markup=auth_markup)
        

@dp.message_handler(content_types=ContentTypes.CONTACT)
async def add_contact(message: Message):
    user_id = message.contact.user_id
    username = message.chat.username
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    phone = message.contact.phone_number
    registrstion_users(user_id, username, first_name, last_name, phone)

    information = f"Айди: {user_id}\nПол(кое) Имя: @{username}\nИмя: {first_name}\nФамилия: {last_name}\nНомер: {phone}\nВремя записи: {datetime.now().strftime('%Y-%m-%d')}"
    await bot.send_message(chat_id=ADMIN_USERID, text=information)
    await message.reply(text="Вы были зарегистрированы в нашем сервисе, пользуйтесь на здоровье 😇", reply_markup=auth_markup)


# 
@dp.inline_handler()
async def inline_query(inline_query: InlineQuery):
    text = inline_query.query
    results = search_inline_mode(text)

    articles = []
    for result in results:
        article = InlineQueryResultArticle(
            id = f"{result[0]}",
            title = f"{result[2]}",
            description = f"{result[3]}",
            url = f"{result[5]}",
            input_message_content = InputTextMessageContent(message_text = "hello")
        )
        articles.append(article)
        if len(articles) == 50:
            break
    
    await inline_query.answer(articles, cache_time=1, is_personal=True)




if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass