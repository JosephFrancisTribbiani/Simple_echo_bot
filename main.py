import telebot
from os import environ
from dotenv import load_dotenv

# загружаем переменные окружения из файла .env
load_dotenv()
TOKEN = environ.get('TOKEN')

# создаем обьект bot
bot = telebot.TeleBot(token=TOKEN)


# обработчик сообщений, который на любое текстовое сообщение от пользователя
# отвечает 'Привет, я бот'
@bot.message_handler(content_types=["text"])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, я бот')


# main функция с polling
# наш бот постоянно бегает на сервер Telegram с вопросом "Для меня есть сообщения?"
def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
