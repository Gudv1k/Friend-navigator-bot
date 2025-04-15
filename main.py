# Функция приветствия
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 Привет! Это бот для подготовки к экзамену IELTS.\n\n"
        "Выбери команду:\n"
        "/lessons — Начать обучение\n"
        "/test — Пройти тест IELTS\n"
        "/progress — Посмотреть прогресс\n"
        "/help — Инструкция и помощь"
    )

    keyboard = ReplyKeyboardMarkup([['/lessons', '/test'], ['/progress', '/help']], resize_keyboard=True)

    await update.message.reply_text(welcome_text, reply_markup=keyboard)
