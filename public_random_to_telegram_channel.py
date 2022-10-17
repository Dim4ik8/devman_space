import telegram
import os
from dotenv import load_dotenv
import argparse
import random


def main():
    load_dotenv()
    token = os.environ['TOKEN_FOR_NASA']
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    parser = argparse.ArgumentParser(
        description='Публикуем фото в телеграмм канал'
    )

    parser.add_argument('path', help='Введите путь к публикуемому фото', nargs='?', default='images/')

    args = parser.parse_args()
    path = args.path

    bot = telegram.Bot(token=telegram_token)
    chat_id = os.environ['CHANNEL_ID']

    if os.path.isfile(path):
        bot.send_document(chat_id=chat_id, document=open(path, 'rb'))
    else:
        random_photo = random.choice(os.listdir('images'))
        bot.send_document(chat_id=chat_id, document=open(f'images/{random_photo}', 'rb'))


if __name__ == '__main__':
    main()
