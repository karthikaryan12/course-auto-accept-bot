import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("7898349005:AAGnYnhIgODx3iIAC4l7yWDd_Fgr-y8F9G8")  # Railway will store this value

async def start(update, context):
    await update.message.reply_text("Bot is online and running 24/7!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
