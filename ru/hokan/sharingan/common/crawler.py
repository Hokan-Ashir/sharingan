import logging
import os
import urllib2
from StringIO import StringIO
from abc import abstractmethod, ABCMeta
from multiprocessing.dummy import Pool as ThreadPool
from string import lower

import requests
from PIL import Image
from lxml.html import document_fromstring


class Crawler:
    __metaclass__ = ABCMeta

    __output_directory = ''
    __target_url = ''
    __NUMBER_OF_THREADS = 10

    def __init__(self, target_url, output_directory):
        self.__target_url = target_url
        self.__output_directory = output_directory
        pass

    @abstractmethod
    def _get_random_url_name(self):
        pass

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
            data = url_data.read()
            url_data.close()
            document = document_fromstring(data)
            image_target_url = document.xpath('//img[contains(@class, \'image__pic js-image-pic\')]/@src')[0]
            if not image_target_url:
                logging.debug('No image exists in url: ' + full_image_url)
                return

            response = requests.get(image_target_url)
            try:
                img = Image.open(StringIO(response.content))
            except Exception as e:
                logging.debug('No image exists in url: ' + full_image_url + ' reason: ' + str(e.message))
                return

            image_name = str(image_target_url).rsplit('/', 1)[1]
            image_file_path = self.__output_directory + image_name
            if [image_file_path[-len(img.format):] != lower(img.format)]:
                image_file_path += '.' + lower(img.format)
            try:
                img.save(image_file_path)
            except KeyError as e:
                logging.debug('Can\'t save image from url: ' + full_image_url + ' reason: ' + str(e.message))

        except urllib2.HTTPError as e:
            logging.debug('Failed to filter url: ' + full_image_url + ' reason: ' + str(e.getcode()))

    def get_pictures(self, number_of_pictures):
        if not os.path.exists(self.__output_directory):
            os.makedirs(self.__output_directory)

        pictures_per_thread = number_of_pictures / self.__NUMBER_OF_THREADS
        pool = ThreadPool(self.__NUMBER_OF_THREADS)
        pool.map(self.__get_pictures_separate_thread, [pictures_per_thread] * self.__NUMBER_OF_THREADS)
