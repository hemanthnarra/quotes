from telegram import Update
from telegram.ext import *
import requests
import json
import constants
import os

def start(update, context):
    user = update.message.chat_id
    context.bot.send_message(chat_id=user, text=constants.start_text)

def get_quote():
    url = 'https://api.quotable.io/random?tags=business|success'
    contents = requests.get(url).json()
    quote_text = contents['content']
    return quote_text

def quote(context):
    text = get_quote()
    context.bot.send_message(chat_id='@hemanthkumarnarra', text=text)

def main():
    bot_token = os.environ.get('BOT_TOKEN','')
    updater = Updater(bot_token, use_context=True)
    job_queue = JobQueue()
    dp = updater.dispatcher
    job_queue.set_dispatcher(dp)
    job_queue.run_repeating(callback=quote, interval=60)
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    # updater.idle()
    job_queue.start()

if __name__ == '__main__':
    main()