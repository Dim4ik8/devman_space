import urllib.parse

import requests
import os
from urllib.parse import urlparse
import datetime


def save_picture(url, path):
    directory = path
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, path):
    response = requests.get(url)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    directory = path
    if not os.path.exists(directory):
        os.makedirs(directory)

    for number, photo in enumerate(photos):
        with open(f'{directory}/spacex_{number}', 'wb') as file:
            file.write(response.content)


def get_extension(url):
    if '.' in urlparse(url).path:
        return urlparse(url).path.split('.')[-1]


def get_some_photos_from_NASA(count, path):
    count = count
    API_for_NASA = 'O9o85vTmNfadhABiMevAgQ3VdbxE05NUq7I4HcA2'
    url = f'https://api.nasa.gov/planetary/apod?count={count}&api_key={API_for_NASA}'
    photos = requests.get(url).json()
    directory = path

    for num, photo in enumerate(photos):
        if not os.path.exists(directory):
            os.makedirs(directory)
        response = requests.get(photo['url'])
        ext = get_extension(photo['url'])
        with open(f'{directory}/spacex_{num}.{ext}', 'wb') as file:
            file.write(response.content)


def get_epic_from_nasa(date, path):
    API_for_NASA = 'O9o85vTmNfadhABiMevAgQ3VdbxE05NUq7I4HcA2'
    url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={API_for_NASA}'

    date_for_photo = datetime.date.fromisoformat(urlparse(url).path.split('/')[-1])

    year = date_for_photo.year
    month = date_for_photo.strftime('%m')
    day = date_for_photo.strftime('%d')

    pictures = requests.get(url).json()
    directory = path

    if pictures:
        for number, picture in enumerate(pictures):
            if not os.path.exists(directory):
                os.makedirs(directory)
            image = picture['image']
            response = requests.get(
                f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png?api_key={API_for_NASA}')
            with open(f'{directory}/nasa_apod_{number}.png', 'wb') as file:
                file.write(response.content)

    else:
        print(f'Извините, {day}.{month}.{year} снимков Земли не делалось ..')


def main():
    get_epic_from_nasa('2019-02-28', 'stones')


if __name__ == '__main__':
    main()
