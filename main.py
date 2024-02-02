import os
import telebot
from telebot import types
import threading
import time
from first_telegram_bot.api import TOKEN
from first_telegram_bot.thread import NumThread
bot=telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def handle_number(message):
    try:
        text_from_user = int(message.text)
        if text_from_user.isdigit() :
            number=text_from_user
            if int(number)>0:
                newThread=NumThread(number,message.chat.id,bot)
                newThread.start()
                bot.send_message(message.chat.id,'counting started')
            else:
                bot.reply_to(message, "Please enter a non-negative number.")
        else:
            pass 
            
    except ValueError:
        bot.reply_to(message, "Invalid input. Please enter a valid things.")

if __name__ == "__main__":
    bot.polling()
