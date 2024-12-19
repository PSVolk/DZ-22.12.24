#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import re
import telebot
from telebot import types

API_TOKEN = '7684324256:AAGLrK8CVtZyQFvtdLv3IMQDt0gMuR9ddCY'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['button'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("? Замена масла")
    btn2 = types.KeyboardButton("❓ Шиномонтаж")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери услугу".format(message.from_user), reply_markup=markup)
# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я долго ждал, пока ты мне напишешь!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)

def start(message): #Начало
	if message.text.lower() == 'вычисли сумму чисел' or message.text.lower() == '/sum':#Команда для начала. message.text - получаемый текст. lower(), значит не учитывается регистр, т.е. и /SUM и /SuM будет считаться за один и тот же текст
		bot.send_message(message.from_user.id, 'Хорошо. Введи два числа которые ты хочешь суммировать. К примеру "1 и 5".')
		bot.register_next_step_handler(message, sumcalc)#"Перенаправляет" на след.функцию
	else:
		bot.send_message(message.from_user.id, 'Введи /sum, или напиши "Вычисли сумму чисел", чтобы продолжить.')

def sumcalc(message):#После "перенаправления" функция сработает, лишь после получения message
    number1, number2 = re.split(' и ', message.text, maxsplit = 1)
    number1 = int(number1) #Проверка "числа ли?" полученные данные. Если без такой проверки. То при попытке сделать сумму, а там не числа - то краш
    number2 = int(number2)
    bot.send_message(message.from_user.id, 'Сумма двоих введённых тобой чисел равна - ' + str(number1 + number2))


def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()