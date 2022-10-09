import requests
import os


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


def main():
    spaceX = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'

    fetch_spacex_last_launch(spaceX, 'images')


if __name__ == '__main__':
    main()
