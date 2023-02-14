import telebot
from environs import Env
from datetime import datetime

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from translate import Translator

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
pink_translate_bot = telebot.TeleBot(BOT_TOKEN)


# Star message
@pink_translate_bot.message_handler(commands=["start"])
def star_message(message):
    pink_translate_bot.send_message(message.chat.id, f"Hi {message.from_user.first_name} enter your born year", )
    pink_translate_bot.register_next_step_handler(message, get_message)


@pink_translate_bot.message_handler(chat_types=['text'])
def get_message(message):
    try:
        int(message.text)
    except Exception:
        pink_translate_bot.send_message(message.chat.id, f"Some error")
    else:
        pink_translate_bot.send_message(message.chat.id,
                                        f" your are  {int(datetime.today().strftime('%Y')) - int(message.text)} years old")


if __name__ == '__main__':
    pink_translate_bot.infinity_polling()
