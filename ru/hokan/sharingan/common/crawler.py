import logging
import os
from StringIO import StringIO
from abc import abstractmethod, ABCMeta
from multiprocessing.dummy import Pool as ThreadPool

import requests
from PIL import Image


class Crawler:
    __metaclass__ = ABCMeta

    __output_directory = ''
    __target_url = ''
    __image_extensions = ['.jpg', '.png']
    __NUMBER_OF_THREADS = 10

    def __init__(self, target_url, output_directory):
        self.__target_url = target_url
        self.__output_directory = output_directory
        pass

    @abstractmethod
    def _get_random_image_name(self):
        pass

    @abstractmethod
    def _should_image_be_processed(self, full_image_url):
        return True

    def __get_pictures_separate_thread(self, number_of_pictures):
        for x in xrange(0, number_of_pictures):
            for extension in self.__image_extensions:
                if self.__try_to_download_picture(extension):
                    break

    def __try_to_download_picture(self, file_extension):
        image_name = self._get_random_image_name() + file_extension
        full_image_url = self.__target_url + image_name
        logging.debug('Trying to process url: ' + full_image_url)
        if not self._should_image_be_processed(full_image_url):
            return False
        logging.debug('Filtering passed for url: ' + full_image_url)

        response = requests.get(full_image_url)
        img = Image.open(StringIO(response.content))
        img.save(self.__output_directory + image_name)

        return True

    def get_pictures(self, number_of_pictures):
        if not os.path.exists(self.__output_directory):
            os.makedirs(self.__output_directory)

        pictures_per_thread = number_of_pictures / self.__NUMBER_OF_THREADS
        pool = ThreadPool(self.__NUMBER_OF_THREADS)
        pool.map(self.__get_pictures_separate_thread, [pictures_per_thread] * self.__NUMBER_OF_THREADS)
