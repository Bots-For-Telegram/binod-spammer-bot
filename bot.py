from telegram.ext import Updater , CommandHandler, MessageHandler, Filters
import logging
import os
import time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = os.environ.get("TOKEN")
PORT = int(os.environ.get("PORT",5000))
APP = "binod-spammer-bot"
updater = Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
def spam(update,context):
  for j in range(5):
    for i in range(20):
      context.bot.sendMessage(update.message.chat_id,text="Binod")
      time.sleep(0.9)
    time.sleep(60)

spam_handler = MessageHandler((~Filters.command),spam)
dispatcher.add_handler(spam_handler)
updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
updater.bot.setWebhook("https://"+APP +".herokuapp.com/" + TOKEN)
    #updater.start_polling()
updater.idle()
