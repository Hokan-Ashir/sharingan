import os
import urllib2
from StringIO import StringIO
from abc import abstractmethod, ABCMeta
from multiprocessing.dummy import Pool as ThreadPool

import requests
from PIL import Image


class Crawler:
    __metaclass__ = ABCMeta

    __output_directory = ''
    __target_url = ''
    __IMAGE_EXTENSION = '.png'
    __NUMBER_OF_THREADS = 10
    __REMOVED_IMAGE_URL = 'http://i.imgur.com/removed.png'

    def __init__(self, target_url, output_directory):
        self.__target_url = target_url
        self.__output_directory = output_directory
        pass

    @abstractmethod
    def _get_random_image_name(self):
        pass

    def __get_pictures_separate_thread(self, number_of_pictures):
        for x in xrange(0, number_of_pictures):
            image_name = self._get_random_image_name() + self.__IMAGE_EXTENSION
            full_image_url = self.__target_url + image_name
            try:
                img_data = urllib2.urlopen(full_image_url)
                if [img_data.url == self.__REMOVED_IMAGE_URL]:
                    # TODO add logging or some other notification
                    continue
            except urllib2.HTTPError:
                # TODO add logging or some other notification
                continue

            response = requests.get(full_image_url)
            img = Image.open(StringIO(response.content))
            img.save(self.__output_directory + image_name)

    def get_pictures(self, number_of_pictures):
        if not os.path.exists(self.__output_directory):
            os.makedirs(self.__output_directory)

        pictures_per_thread = number_of_pictures / self.__NUMBER_OF_THREADS
        pool = ThreadPool(self.__NUMBER_OF_THREADS)
        pool.map(self.__get_pictures_separate_thread, [pictures_per_thread] * self.__NUMBER_OF_THREADS)
