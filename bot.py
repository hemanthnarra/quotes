from telegram import update
from telegram.ext import Updater, dispatcher, CommandHandler
import requests
import os

def get_quote():
    contents = requests.get('https://free-quotes-api.herokuapp.com/').json()
    required = contents['quote']
    return required

def quote(update, context):
    required = get_quote()
    chat_id = '-1001496045934'
    context.bot.send_message(chat_id=chat_id,text=required)

def main():
    bot_token = os.environ.get('BOT_TOKEN','')
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('quote', quote))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()