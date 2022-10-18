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
        with open(path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    else:
        random_photo = random.choice(os.listdir('images'))
        with open(f'images/{random_photo}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)


if __name__ == '__main__':
    main()
