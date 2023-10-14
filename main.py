from telegram.ext import *
from telegram import *

bot = Bot("api")

updater = Updater("api", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("HellO! Welcome to TestBot")


def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various features of testbot
        /bestdeals -> Best deals from Ecommerce sites
        /cricket -> cricket match predictions
        /weather -> Daily weather updates
        """
    )


def content(update, context):
    update.message.reply_text(" Bro!! we are just getting started")


def bestdeals(update, context):
    update.message.reply_text("Link : https://t.me/Amazon_Best_Deals_Flipkart_Loot")


def cricket(update, context):
    update.message.reply_text("Link : https://t.me/WORLD_CRICKET_PREDICTIONS_CUP")


def weather(update, context):
    update.message.reply_text("Link : https://t.me/indialiveweatherandnews")


def contact(update, context):
    update.message.reply_text("You can contact me directly through my main ID")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('bestdeals', bestdeals))
dispatcher.add_handler(CommandHandler('cricket', cricket))
dispatcher.add_handler(CommandHandler('weather', weather))
dispatcher.add_handler(CommandHandler('contact', contact))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('content', content))

updater.start_polling()
updater.idle()
