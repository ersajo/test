import shutil
import requests

response = requests.get('http://lorempixel.com/400/200', stream=True)
response.raise_for_status()
response.raw.decode_content = True  # Required to decompress gzip/deflate compressed responses.
with open('img.png','wb') as img:
    shutil.copyfileobj(response.raw, img)
del response

with open('img.png','rb') as lectura:
    entrada = lectura.read()

print len(entrada)
print entrada[684]
