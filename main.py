import telebot
from os import environ
from dotenv import load_dotenv
from flask import Flask, request

# загружаем переменные окружения из файла .env
load_dotenv()
TOKEN = environ.get('TOKEN')
PORT = int(environ.get('PORT', 5000))  # второе значение по умолчанию, если не будет найдено первое

# создаем обьект bot и обьект server
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


# обработчик сообщений, который на любое текстовое сообщение от пользователя
# отвечает 'Привет, я бот'
@bot.message_handler(content_types=["text"])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, я бот')


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-app-hse.herokuapp.com/' + TOKEN)
    return "!", 200


# main функция с Web Hook
# наш бот смиренно ждет сообщение от Telegram
def main():
    server.run(host="0.0.0.0", port=PORT)


if __name__ == '__main__':
    main()
