from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Приветственная функция
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 Привет! Это бот для подготовки к экзамену IELTS.\n\n"
        "Выбери команду:\n"
        "/lessons — Начать обучение\n"
        "/test — Пройти тест IELTS\n"
        "/progress — Посмотреть прогресс\n"
        "/help — Инструкция и помощь"
    )

    keyboard = ReplyKeyboardMarkup(
        [['/lessons', '/test'], ['/progress', '/help']],
        resize_keyboard=True
    )

    await update.message.reply_text(welcome_text, reply_markup=keyboard)

# Основной запуск
def main():
    application = Application.builder().token("8106959752:AAE-G0EcQJ31jEFZjgWuv9hMsdHgfMU2df4").build()

    application.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
