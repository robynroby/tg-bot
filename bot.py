import Constants as keys
import random
from threading import Thread
from telegram import Bot
from telegram.ext import *
import time

print('The Bot is starting....')


async def start_command(update, context):
    await update.message.reply_text('Hello! Welcome To Aviator Predictor!.\nJoin us as we get rich from these sure aviator predictions\nUtavuna Unono')

async def get_random_command(update, context):
    await update.message.reply_text(f'⏱️Time: 23:14⏱️ \n⚡ Cashout at {random.randint(1, 100)}x ⚡')

if __name__ == '__main__':
    application = Application.builder().token(keys.API_KEY).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('get_random', get_random_command))



    # Run bot
    application.run_polling()
