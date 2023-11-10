import telebot
import utils
from telebot import types  # для указание типов
bot = telebot.TeleBot("6480715477:AAF0w8AQeVTVepQ2XtKMEwiEuFcd2iafHno")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть рейтинг")
    btn2 = types.KeyboardButton("Начать тест")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для обучения, введите имя".format(
                         message.from_user))
    def name():
        pass #заносится в базу данных
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Посмотреть рейтинг"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
        def see():
            pass

    elif (message.text == "Начать тест"):
        def test():
            pass
    elif (message.text == "Мои данные"):
        def data():
            pass

bot.polling(none_stop=True)