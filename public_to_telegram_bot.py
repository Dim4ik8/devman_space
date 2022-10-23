import os
from dotenv import load_dotenv
import argparse
from help import publication_to_telegram


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    parser = argparse.ArgumentParser(
        description='Публикуем фотографии в телеграмм канал'
    )
    parser.add_argument('path', help='Введите название папки, из которой будут опубликованы фото', nargs='?',
                        default='images')
    parser.add_argument('sec', help='Введите задержку для опубликования фото в секундах', nargs='?', default='3600')

    args = parser.parse_args()
    path = args.path
    sec = int(args.sec)

    chat_id = os.environ['TG_CHAT_ID']

    if os.path.isdir(path):
        publication_to_telegram(path, chat_id, telegram_token, sec)

    else:
        print('Папка не найдена, укажите верный путь до фото! ')


if __name__ == '__main__':
    main()
