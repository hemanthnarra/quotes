from telegram import update
from telegram.ext import Updater, dispatcher, CommandHandler
import requests
import os

def get_quote():
    contents = requests.get('https://free-quotes-api.herokuapp.com/').json()
    required = contents['quote']
    return required

def quote(update, context):
    chat_id = update.message.chat_id
    if chat_id == '705433594':
        required = get_quote()
        chat_id = '-1001496045934'
        context.bot.send_message(chat_id=chat_id,text=required)
    else:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id,text='sorry! only hemanth can perform this action')

def main():
    bot_token = os.environ.get('BOT_TOKEN','')
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('quote', quote))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()