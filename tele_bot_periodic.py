from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue
from telegram import Update
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')

async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    url = 'http://127.0.0.1:5000'
    response = requests.get(url)
    if response.status_code == 200:
        await context.bot.send_message(job.chat_id, text=f"{response.json().get('message')}")
        

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_message.chat_id
    try:
        context.job_queue.run_repeating(alarm, interval=10, first=2, chat_id=chat_id, name=str(chat_id))
        await update.effective_message.reply_text('Timer set')
    except (IndexError, ValueError):
        await update.effective_message.reply_text("Error Gang")

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("set", set_timer))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()