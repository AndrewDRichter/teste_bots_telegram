import os
from decouple import config
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# dados de configuração da api

BOT_TOKEN = config('BOT_TOKEN', cast=str)
bot = telebot.TeleBot(BOT_TOKEN)

HELP_MESSAGE = """
Test paragraph message,
Here will be the help section.
"""

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello and welcome.")
    bot.reply_to(message, "Type /help to know more about this bot")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGE)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)

bot.infinity_polling()