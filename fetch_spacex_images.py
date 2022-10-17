import requests
import os
from dotenv import load_dotenv
import argparse
from pathlib import Path


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Сохраняем фотографии запуска'
    )
    parser.add_argument('path', help='Введите название папки, куда будут сохранены фото')
    parser.add_argument('launch', help='Введите ID запуска', nargs='?', default='latest')

    args = parser.parse_args()
    path = args.path
    launch = args.launch

    url = f'https://api.spacexdata.com/v5/launches/{launch}'

    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    if photos:
        os.makedirs(path, exist_ok=True)

        for number, photo in enumerate(photos):
            response = requests.get(photo)
            filename = Path.cwd() / path / f'spacex_{number}.jpg'
            with open(filename, 'wb') as file:
                file.write(response.content)
    else:
        print('Извините, на выбранном запуске фотографии не делались..')


if __name__ == '__main__':
    main()
