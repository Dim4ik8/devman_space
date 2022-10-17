# from urllib.parse import urlparse
#
# def get_extension(url):
#     if '.' in urlparse(url).path:
#         return urlparse(url).path.split('.')[-1]
import os

os.makedirs('images', exist_ok=True)