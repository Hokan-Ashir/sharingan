import logging
import os
import random
import string
import urllib2

from ru.hokan.sharingan.common.crawler import Crawler


class ImgurCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 7
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_imgur' + os.path.sep
    __TARGET_URL = 'http://i.imgur.com/'
    __REMOVED_IMAGE_URL = 'http://i.imgur.com/removed.png'
    __REMOVED_IMAGE_FAILURE_REASON = 'image was removed'

    def __init__(self):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY)

    def _get_random_image_name(self):
        return ''.join(random.choice(string.letters + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))

    def _should_image_be_processed(self, full_image_url):
        img_data = urllib2.urlopen(full_image_url)
        url = img_data.url
        image_url = url == self.__REMOVED_IMAGE_URL
        if image_url:
            logging.debug('Failed to filter url: ' + full_image_url + ' reason: ' + self.__REMOVED_IMAGE_FAILURE_REASON)
            return False

        return True
