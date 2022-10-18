from urllib.parse import urlparse


def get_extension(url):
    if '.' in urlparse(url).path:
        return urlparse(url).path.split('.')[-1]

# count = '2'
# token = '73yi3hg5j3hg'
# # url = https://api.nasa.gov/planetary/apod?count={count}&api_key={token}
# params = {'count': count, 'api_key': token }
# url = 'https://api.nasa.gov/planetary/apod'
#
# response = requests.get(url, params=params)
# print(requests.get(url, params=params))