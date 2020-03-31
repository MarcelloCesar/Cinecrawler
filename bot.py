import os
import telebot
import urllib
import json

bot = telebot.TeleBot("936831786:AAEcz9i8g2FKLWG2j8g5Nf93v-g-y5X3F0A")

@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.reply_to(message, "starting")


bot.polling()