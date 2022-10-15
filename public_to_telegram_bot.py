import time
import requests
import telegram
import os
from dotenv import load_dotenv
import argparse
from help import get_extension


def main():
    load_dotenv()
    token = os.getenv('TOKEN_FOR_NASA')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    parser = argparse.ArgumentParser(
        description='Сохраняем фотографии APOD и публикуем в телеграмм канал'
    )
    parser.add_argument('path', help='Введите название папки, куда будут сохранены фото')
    parser.add_argument('count', help='Введите количество фото для сохранения и публикования', nargs='?', default='1')

    args = parser.parse_args()
    path = args.path
    count = args.count

    url = f'https://api.nasa.gov/planetary/apod?count={count}&api_key={token}'
    photos = requests.get(url).json()

    for num, photo in enumerate(photos):
        if not os.path.exists(path):
            os.makedirs(path)
        response = requests.get(photo['url'])
        ext = get_extension(photo['url'])
        with open(f'{path}/spacex_{num}.{ext}', 'wb') as file:
            file.write(response.content)

    bot = telegram.Bot(token=telegram_token)
    chat_id = os.getenv('CHANNEL_ID')

    while True:
        for filename in os.listdir(path):
            f = os.path.join(path, filename)

            if os.path.isfile(f):
                bot.send_document(chat_id=chat_id, document=open(f, 'rb'))
                time.sleep(10)


if __name__ == '__main__':
    main()
