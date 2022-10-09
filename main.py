import urllib.parse

import requests
import os
from urllib.parse import urlparse
from pprint import pprint as pp


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


def main():
    API_for_NASA = 'O9o85vTmNfadhABiMevAgQ3VdbxE05NUq7I4HcA2'
    url = f'https://api.nasa.gov/planetary/apod?count=30&api_key={API_for_NASA}'
    photos = requests.get(url).json()

    for num, photo in enumerate(photos):
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        response = requests.get(photo['url'])
        ext = get_extension(photo['url'])
        with open(f'{directory}/spacex_{num}.{ext}', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    main()
