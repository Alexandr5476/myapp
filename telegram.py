from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


def fnc(text):
    bot.send_message("888281527", text)


def send(text):
    if text != '':
        fnc(text)
