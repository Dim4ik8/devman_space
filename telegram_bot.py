import os

import telegram
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=token)
chat_id = os.getenv('CHANNEL_ID')

bot.send_message(chat_id=chat_id, text="Привет! Вас рад видеть бот!! :))")