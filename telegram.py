import telebot

bot = telebot.TeleBot('6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k')


def send(text):
    if text != '':
        bot.send_message("888281527", text)
