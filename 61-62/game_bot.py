import telebot
import random

token = ''
bot = telebot.TeleBot(token)

start = False
num = 0

@bot.message_handler(commands=['game'])
def start_game(message):
    global start
    global num
    start = True
    bot.reply_to(message, 'Игра началась. Угадай число от 1 до 10.')
    num = random.randint(1, 10)
    return num

@bot.message_handler(regexp=r'^\d+(\.\d+)?$')
def guessing(message):
    global start
    global num
    if start:
        if message.text == str(num):
            bot.reply_to(message, 'Угадал! Игра окончена')
            start = False
        else:
            bot.reply_to(message, 'Не угадал!')

@bot.message_handler(commands=['end'])
def end_game(message):
    global start
    start = False
    bot.reply_to(message, 'Игра окончена')


bot.infinity_polling()