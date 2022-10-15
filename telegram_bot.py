import os

import telegram
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=token)

print(bot.get_me())