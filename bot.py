from telegram.ext import Updater, MessageHandler, Filters

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на свой токен, полученный от BotFather
TOKEN = '7125097349:AAFlPMJvd0lWd8TGyMvEok76fFwEuZRTDlY'

# Обработчик всех сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я простой телеграм-бот на Python.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавляем обработчик всех сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
