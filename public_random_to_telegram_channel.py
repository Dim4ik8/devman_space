import os
from dotenv import load_dotenv
import argparse
import random
from help import send_img_to_telegram
from pathlib import Path


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    parser = argparse.ArgumentParser(
        description='Публикуем фото в телеграмм канал'
    )

    parser.add_argument('path', help='Введите путь к публикуемому фото', nargs='?', default='images/')

    args = parser.parse_args()
    path = args.path

    chat_id = os.environ['TG_CHAT_ID']

    if os.path.isfile(path):
        send_img_to_telegram(path, chat_id, telegram_token)

    else:
        random_photo = random.choice(os.listdir('images'))
        path = Path.cwd() / 'images' / f'{random_photo}'
        send_img_to_telegram(path, chat_id, telegram_token)


if __name__ == '__main__':
    main()
