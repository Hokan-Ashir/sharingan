import os
import random
import string
from StringIO import StringIO
from multiprocessing.dummy import Pool as ThreadPool

import requests
from PIL import Image


class crawler:
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output' + os.path.sep
    __TARGET_URL = 'http://i.imgur.com/'
    __IMAGE_NAME_LENGTH = 7
    __IMAGE_EXTENSION = '.png'
    __NUMBER_OF_THREADS = 10

    @staticmethod
    def __get_random_image_name(length):
        return ''.join(random.choice(string.letters + string.digits) for i in range(length))

    def get_pictures_separate_thread(self, number_of_pictures):
        for x in xrange(0, number_of_pictures):
            image_name = self.__get_random_image_name(self.__IMAGE_NAME_LENGTH) + self.__IMAGE_EXTENSION
            response = requests.get(self.__TARGET_URL + image_name)
            img = Image.open(StringIO(response.content))
            img.save(self.__OUTPUT_DIRECTORY + image_name)

    def get_pictures(self, number_of_pictures):
        if not os.path.exists(self.__OUTPUT_DIRECTORY):
            os.makedirs(self.__OUTPUT_DIRECTORY)

        pictures_per_thread = number_of_pictures / self.__NUMBER_OF_THREADS
        pool = ThreadPool(self.__NUMBER_OF_THREADS)
        pool.map(self.get_pictures_separate_thread, [pictures_per_thread] * self.__NUMBER_OF_THREADS)
