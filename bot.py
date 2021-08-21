from telegram import update
from telegram.ext import Updater, dispatcher, CommandHandler, callbackcontext, JobQueue
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
    bot_token = os.environ.get('BOT_TOKEN','')
    updater = Updater(bot_token, use_context=True)
    job_queue = JobQueue()
    dispatcher = updater.dispatcher
    job_queue.set_dispatcher(dispatcher)
    job_minute = job_queue.run_repeating(quote, interval=60, first=10)
    # dp.add_handler(CommandHandler('quote', quote))
    updater.start_polling()
    job_queue.start()
    # updater.idle()

if __name__ == '__main__':
    main()