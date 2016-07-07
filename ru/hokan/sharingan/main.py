import os
import random
import string
from StringIO import StringIO

import requests
from PIL import Image

OUTPUT_DIRECTORY = '.' + os.path.sep + 'output' + os.path.sep


def get_random_image_name(length):
    return ''.join(random.choice(string.letters + string.digits) for i in range(length))


def get_some_pictures(number_of_pictures):
    for x in xrange(0, number_of_pictures):
        image_name = get_random_image_name(7) + '.png'
        response = requests.get('http://i.imgur.com/' + image_name)
        img = Image.open(StringIO(response.content))
        img.save(OUTPUT_DIRECTORY + image_name)

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    get_some_pictures(1)
