import requests
from pathlib import Path
import telegram
import os
import time


def save_pictures(url, path, num, ext, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    filename = Path.cwd() / path / f'space_{num}{ext}'
    with open(filename, 'wb') as file:
        file.write(response.content)


def send_img_to_telegram(path, chat_id, token):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def publication_to_telegram(path, chat_id, token, sec):
    while True:
        for filename in os.listdir(path):
            f = os.path.join(path, filename)

            try:
                if os.path.isfile(f):
                    send_img_to_telegram(f, chat_id, token)
            except ConnectionError:
                continue
            time.sleep(sec)
