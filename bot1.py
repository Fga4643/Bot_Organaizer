import telebot
import requests
from telebot import types
from telebot.types import InputMediaPhoto
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import admins
import json
import os
import threading
token="5104970683:AAHxn5HN4igeHRa51misrrh3z-hKtASvksQ"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    if int(message.chat.id) in admins:
        bot.send_message(message.chat.id, 'Сделано, введите:')
        bot.send_message(message.chat.id, '#$%#$:@#$%^&@')
        os.system("py C:/Users/Fga4643/Desktop/Хакатон/BOTPOST.py")
        bot.send_message(message.chat.id, 'Сделано, введите:')


@bot.message_handler(content_types=['text'])
def main_message(message):
    try:
        if message.text == "start" and int(message.chat.id) in admins:
            os.system("py C:/Users/Fga4643/Desktop/Хакатон/BOTPOST.py")
            bot.send_message(message.chat.id, 'Сделано, введите:')
            bot.send_message(message.chat.id, '#$%#$:@#$%^&@')         
    except:
        pass      
      

    
            
if __name__ == '__main__':
    bot.polling(none_stop=True)