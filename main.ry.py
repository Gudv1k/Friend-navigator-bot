
import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != ALLOWED_USER_ID:
        return
    bot.reply_to(message, "Привет, Андрей! Связь установлена. Я буду уведомлять тебя о ходе проекта Friend.")

bot.infinity_polling()
