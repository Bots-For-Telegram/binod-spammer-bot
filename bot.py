from telegram.ext import Updater , CommandHandler, MessageHandler, Filters
import logging
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = os.environ.get("TOKEN")
PORT = int(os.environ.get("PORT",5000))
APP = ""
updater = Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
def spam(update,context):
  for i in range(100):
    context.bot.sendMessage(update.message.chat_id,text="Binod")
spam_handler = MessageHandler((~Filters.command),spam)
dispatcher.add_handler(spam_handler)
updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
updater.bot.setWebhook("https://"+APP +".herokuapp.com/" + TOKEN)
    #updater.start_polling()
updater.idle()