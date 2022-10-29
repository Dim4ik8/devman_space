import requests
from pathlib import Path
import telegram
import os
import time


def save_pictures(url, path, title, num, ext, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    filename = Path.cwd() / path / f'{title}_{num}{ext}'
    with open(filename, 'wb') as file:
        file.write(response.content)


def send_img_to_telegram(path, chat_id, token):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


def collect_files_in_dir_path(path):
    files = []
    for filename in os.listdir(path):
        files.append(Path.cwd() / path / filename)
    return files


def publication_to_telegram(path, chat_id, token, sec):
    files = collect_files_in_dir_path(path)
    while True:
        try:
            for file in files:
                send_img_to_telegram(file, chat_id, token)
        except telegram.error.NetworkError:
            time.sleep(30)
            continue
        time.sleep(sec)
