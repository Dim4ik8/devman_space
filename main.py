import urllib.parse

import requests
import os
from urllib.parse import urlparse
import datetime
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




def get_extension(url):
    if '.' in urlparse(url).path:
        return urlparse(url).path.split('.')[-1]





def main():
    pass

if __name__ == '__main__':
    main()
