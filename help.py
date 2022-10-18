from urllib.parse import urlparse
import requests
from pathlib import Path

def get_extension(url):
    if '.' in urlparse(url).path:
        return urlparse(url).path.split('.')[-1]

def save_pictures(url, path, num, ext):
    response = requests.get(url)
    response.raise_for_status()
    filename = Path.cwd() / path / f'spacex_{num}.{ext}'
    with open(filename, 'wb') as file:
        file.write(response.content)
