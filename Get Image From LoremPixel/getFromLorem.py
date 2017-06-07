import shutil
import requests

response = requests.get('http://lorempixel.com/400/200', stream=True)
response.raise_for_status()
response.raw.decode_content = True  # Required to decompress gzip/deflate compressed responses.
with open('img.jpg','wb') as img:
    shutil.copyfileobj(response.raw, img)
del response
