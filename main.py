import requests
import os

def save_picture(url, path):
    directory = path
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)

def main():
    pass

if __name__ == '__main__':
    main()
