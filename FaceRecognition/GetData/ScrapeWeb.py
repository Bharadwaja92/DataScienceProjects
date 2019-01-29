import base64
import io
import requests
import cv2

from bs4 import BeautifulSoup
from PIL import Image

search_term = 'Mehreen_pirzada'
num_pics = 50
domain = 'www.google.com'
path = '/search'
params = {'tbm': 'isch', 'q': search_term}
stored = 0

while stored < num_pics:
    url = 'https://' + domain + path + '?'
    for key, value in params.items():
        url += key + '=' + value.replace(' ', '+') + '&'
    response = requests.get(url=url)
    page = BeautifulSoup(response.text, 'lxml')

    images = page.findAll('img')
    x = 0
    for img in images:
        image_bytes = requests.get(img['src']).content
        image = base64.b64encode(image_bytes)
        image = base64.b64decode(image)
        image = Image.open(io.BytesIO(image))
        print(image, type(image))
        image.save(io.BytesIO(), format='jpeg')
        image.save(search_term + 'image' + str(x) + '.png')
        print('x is', x)
        x += 1

    stored += x

    if stored > num_pics:
        break


