import telegram


bot = telegram.Bot(token='1427700541:AAFZ_Nj3TYlGbU0lMezoiNA24jWOR65_-0E')
# print(bot.getMe())

updates = bot.getUpdates()
print(updates[1])

bot.sendMessage(text='hello,hemanth', chat_id=705433594)