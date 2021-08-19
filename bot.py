from telegram import update
from telegram.ext import Updater, dispatcher, CommandHandler, callbackcontext
import requests
import os

def get_quote():
    contents = requests.get('https://free-quotes-api.herokuapp.com/').json()
    required = contents['quote']
    return required

def quote(context: callbackcontext):
    required = get_quote()
    channel_id = '-1001496045934'
    context.bot.send_message(chat_id=channel_id,text=required)
    
def main():
    bot_token =    os.environ.get('BOT_TOKEN','')
    updater = Updater(bot_token, use_context=True)
    job_queue = updater.job_queue
    job_minute = job_queue.run_repeating(quote, interval=200, first=10)
    # dp = updater.dispatcher
    # dp.add_handler(CommandHandler('quote', quote))
    updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()