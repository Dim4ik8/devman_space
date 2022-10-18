import requests
import os
from dotenv import load_dotenv
import argparse
from help import get_extension, save_pictures
from pathlib import Path


def main():
    load_dotenv()
    token = os.environ['TOKEN_FOR_NASA']
    parser = argparse.ArgumentParser(
        description='Сохраняем фотографии APOD'
    )
    parser.add_argument('path', help='Введите название папки, куда будут сохранены фото')
    parser.add_argument('count', help='Введите количество фото для сохранения', nargs='?', default='1')

    args = parser.parse_args()
    path = args.path
    count = args.count

    url = 'https://api.nasa.gov/planetary/apod'
    params = {'count': count, 'api_key': token}
    photos = requests.get(url, params=params).json()

    for num, photo in enumerate(photos):
        os.makedirs(path, exist_ok=True)
        ext = get_extension(photo['url'])
        save_pictures(photo['url'], path, num, ext)


if __name__ == '__main__':
    main()
