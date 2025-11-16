from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "7898349005:AAGnYnhIgODx3iIAC4l7yWDd_Fgr-y8F9G8"

def start(update, context):
    update.message.reply_text("Bot is running")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
