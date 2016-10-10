import logging
import os
import urllib2
import uuid
from StringIO import StringIO
from abc import abstractmethod, ABCMeta
from multiprocessing.dummy import Pool as ThreadPool
from string import lower

import requests
from PIL import Image
from pytesseract import image_to_string
from pytesseract.pytesseract import TesseractError

from ru.hokan.sharingan.common.Configuration import Configuration


class Crawler:
    __metaclass__ = ABCMeta

    __should_extract_text = False
    __output_directory = ''
    __target_url = ''
    __NUMBER_OF_THREADS = 10

    def __init__(self, target_url, output_directory, should_extract_text):
        self.__target_url = target_url
        self.__output_directory = output_directory
        self.__should_extract_text = should_extract_text
        pass

    @abstractmethod
    def _get_random_url_name(self):
        pass

    def __should_image_be_processed(self, image):
        width, height = image.size

        configuration = Configuration()
        min_width = configuration.get_min_width()
        max_width = configuration.get_max_width()
        min_height = configuration.get_min_height()
        max_height = configuration.get_max_height()

        min_width_passed = True if min_width is None else height >= min_width
        max_width_passed = True if max_width is None else width <= max_width
        min_height_passed = True if min_height is None else height >= min_height
        max_height_passed = True if max_height is None else height <= max_height

        return min_width_passed and max_width_passed and min_height_passed and max_height_passed

    def __get_pictures_separate_thread(self, number_of_pictures):
        for x in xrange(0, number_of_pictures):
            self.__try_to_download_picture()

    def __try_to_download_picture(self):
        url_name = self._get_random_url_name()
        full_image_url = self.__target_url + url_name
        logging.debug('Trying to process url: ' + full_image_url)
        try:
            req = urllib2.Request(full_image_url, None, {
                'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            url_data = urllib2.urlopen(req)

            image_target_url = self._get_image_url_from_source(url_data)
            if not image_target_url:
                logging.debug('No image exists in url: ' + full_image_url)
                return

            response = requests.get(image_target_url)
            try:
                img = Image.open(StringIO(response.content))
            except Exception as e:
                logging.debug('No image exists in url: ' + full_image_url + ' reason: ' + str(e.message))
                return

            if not self.__should_image_be_processed(img):
                return

            image_file_path = self.__output_directory + str(uuid.uuid4())
            if image_file_path[-len(img.format):] != lower(img.format):
                image_file_path += '.' + lower(img.format)
            try:
                img.save(image_file_path)
            except KeyError as e:
                logging.debug('Can\'t save image from url: ' + full_image_url + ' reason: ' + str(e.message))

            if not self.__should_extract_text:
                return

            try:
                img = Image.open(image_file_path)
                text = image_to_string(img)
                logging.info('Extracted text: \'' + text + '\' from image url: ' + full_image_url)
            except TesseractError as e:
                logging.debug(
                    'Can\'t extract text from image from url: ' + full_image_url + ' reason: ' + str(e.message))

        except urllib2.HTTPError as e:
            logging.debug('Failed to filter url: ' + full_image_url + ' reason: ' + str(e.getcode()))

    @abstractmethod
    def _get_image_url_from_source(self, data):
        pass

    def get_pictures(self, number_of_pictures):
        if not os.path.exists(self.__output_directory):
            os.makedirs(self.__output_directory)

        threads = self.__NUMBER_OF_THREADS
        if number_of_pictures < threads:
            self.__get_pictures_separate_thread(number_of_pictures)
        else:
            pictures_per_thread = number_of_pictures / threads
            number_of_threads = threads
            pool = ThreadPool(number_of_threads)
            pool.map(self.__get_pictures_separate_thread, [pictures_per_thread] * number_of_threads)
