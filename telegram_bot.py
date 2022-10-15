import os

import telegram
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=token)
chat_id = os.getenv('CHANNEL_ID')

bot.send_document(chat_id=chat_id, document=open('images/picture_hello.png', 'rb'))