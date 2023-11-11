import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot("6480715477:AAF0w8AQeVTVepQ2XtKMEwiEuFcd2iafHno")
bot.set_webhook()
import sqlite3

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, username TEXT)''')
def add_user_to_db(user_id, username):
    cursor.execute('INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть рейтинг")
    btn2 = types.KeyboardButton("Начать тест")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для обучения, введите имя".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def name(message):
    user_id = message.from_user.id
    username = message.text
    add_user_to_db(user_id, username)
    bot.send_message(message.chat.id, username)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Привеt")
        def func(message):
            if (message.text == "Посмотреть рейтинг"):
                bot.send_message(message.chat.id, text="Привет")

                def see():
                    pass

            elif (message.text == "Начать тест"):
                def test():
                    pass
            elif (message.text == "Мои данные"):
                def data():
                    pass

bot.polling(none_stop=True)
