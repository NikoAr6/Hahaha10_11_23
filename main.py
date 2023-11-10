import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#kb = ReplyKeyboardMarkup(resize_keyboard=True)

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6480715477:AAF0w8AQeVTVepQ2XtKMEwiEuFcd2iafHno"
#b1 = KeyboardButton('/help')
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
#kb.add(b1)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>"""
#@dp.message(commands=['help'])
#async def help_command(message: types.Message):
#    await message.answer(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
#    await message.delete()
#def start(bot, update):
#    update.message.reply_text('Привет! Я информационный бот компании "Путешествия и туризм".\n'
#                              'Для получения информации можете воспользоваться подсказками ниже!',
#                              reply_markup=markup)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())