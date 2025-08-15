import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from weather import get_weather

load_dotenv()

TG_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello')

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp, feels_like = get_weather()

    text = f"Сейчас на улице {temp}, ощущается как {feels_like}"

    await update.message.reply_text(text)

def handle_response(text):
    return text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(TG_TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('weather', weather_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=5)