import os
import telebot
from logic import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
api=ImgAPI()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Отправьте мнt pfghjc")

@bot.message_handler(commands=['gen'])
def handle_generate(message):
    request = message.text.split(maxsplit=1)[-1] if len(message.text.split()) > 1 else None
    file_path= api.download_image(request)
    with open(file_path, 'rb') as processed_photo:
        bot.send_photo(message.chat.id, processed_photo)

        # Удаляем временные файлы
    os.remove(file_path)
    os.remove(request)

if __name__ == "__main__":
    bot.polling(none_stop=True)