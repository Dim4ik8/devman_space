import urllib.parse

import requests
import os
from urllib.parse import urlparse
from pprint import pprint as pp


def save_picture(url, path):
    directory = path
    if not os.path.exists(directory):
        os.makedirs(directory)
    link = url
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
    return urlparse(url).path.split('.')[-1]


def main():
    url = 'https://apod.nasa.gov/apod/image/2107/LRVBPIX3M82Crop1024.jpg?755=ieutj&uetoe=2435'
    print(get_extension(url))


if __name__ == '__main__':
    main()
