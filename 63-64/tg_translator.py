import telebot
import requests

tg_token = ''
bot = telebot.TeleBot(tg_token)

start = False
text_added = False

@bot.message_handler(commands=['start'])
def start_game(message):
    global start
    start = True
    bot.reply_to(message, 'Привет. Я - бот-переводчик. Чтобы начать перевод текста, введите команду /text.'
                          ' Чтобы завершить работу, введите /end' )

@bot.message_handler(commands=['end'])
def end_translate(message):
    global start
    global text_added
    if start:
        bot.reply_to(message, 'Перевод окончен. Пока!')
        text_added = False
        start = False

@bot.message_handler(commands=['text'])
def get_text(message):
    global start
    global text_added
    if start:
        text_added = True
        bot.reply_to(message, 'Введите текст для перевода. Чтобы завершить работу, введите /end')

@bot.message_handler(func=lambda message: True)
def translate(message):

    y_token = ''
    y_catalog = ''

    global start
    global text_added

    if message == '/end':
        end_translate(message)

    if text_added:

        payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": "en",
            "format": "HTML",
            "texts": [
                f"{message.text}"
            ],
            "folderId": f"{y_catalog}",
            "speller": False
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {y_token}"
        }

        url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        response = requests.post(url, json=payload, headers=headers)
        res = response.json()['translations'][0]['text']
        bot.reply_to(message, res)

bot.infinity_polling()