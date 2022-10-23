import requests
import os
from dotenv import load_dotenv
import argparse
import datetime
from urllib.parse import urlparse
from help import save_pictures


def main():
    load_dotenv()
    token = os.environ['TOKEN_FOR_NASA']
    parser = argparse.ArgumentParser(
        description='Сохраняем фотографии APOD'
    )
    parser.add_argument('path', help='Введите название папки, куда будут сохранены фото', nargs='?', default='images')
    parser.add_argument('date', help='Дата снимков Земли в формате гггг-мм-дд', nargs='?', default='2022-01-01')

    args = parser.parse_args()
    path = args.path
    date = args.date

    url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    params = {'api_key': token}
    date_for_photo = datetime.date.fromisoformat(urlparse(url).path.split('/')[-1])

    year = date_for_photo.year
    month = date_for_photo.strftime('%m')
    day = date_for_photo.strftime('%d')

    pictures = requests.get(url, params=params).json()

    if pictures:
        for number, picture in enumerate(pictures):
            os.makedirs(path, exist_ok=True)

            image = picture['image']
            url_new = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png'

            save_pictures(url_new, path, number, '.png', params)


    else:
        print(f'Извините, {day}.{month}.{year} снимков Земли не делалось ..')


if __name__ == '__main__':
    main()
