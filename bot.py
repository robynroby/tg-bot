import Constants as keys
import random
import asyncio
from threading import Thread
from telegram import Bot
from telegram.ext import Application, CommandHandler
import schedule
import time
from datetime import datetime

print('The Bot is starting....')

chat_id = None  # Initialize a global variable to store the chat ID

# Example image URL or local path
image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFszuVACoh-yAJGqcySlXsea5hIQJPEzZlWA&usqp=CAU'

async def start_command(update, context):
    global chat_id
    chat_id = update.message.chat_id  # Capture the chat ID
    await update.message.reply_text('Hello! Welcome To Aviator Predictor!.\nJoin us as we get rich from these sure aviator predictions\nUtavuna Unono')

async def get_random_command(update, context):
    random_value = round(random.uniform(1, 100), 2)
    current_time = datetime.now().strftime('%H:%M')
    await update.message.reply_text(f'⏱️Time: {current_time}⏱️ \n⚡ Cashout at {random_value}x ⚡')

# A function that sends a message to the user at specified intervals
async def send_message():
    if chat_id:
        bot = Bot(keys.API_KEY)
        random_value = round(random.uniform(1, 100), 2)
        current_time = datetime.now().strftime('%H:%M')
        message_text = f'⏱️Time: {current_time}⏱️ \n⚡ Cashout at {random_value}x ⚡'
        await bot.send_photo(chat_id=chat_id, photo=image_url, caption=message_text)
    else:
        print("Chat ID not set. Please start a conversation with the bot.")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_thread():
    asyncio.run(send_message())

if __name__ == '__main__':
    application = Application.builder().token(keys.API_KEY).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('get_random', get_random_command))
    
    # Schedule the send_message function to run every 1 hour
    schedule.every(60).minutes.do(lambda: asyncio.run(send_message()))

    # Start a thread to run the scheduler
    scheduler_thread = Thread(target=run_schedule)
    scheduler_thread.start()

    # Run bot
    application.run_polling()
