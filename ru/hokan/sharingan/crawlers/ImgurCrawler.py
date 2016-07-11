import os
import random
import string

from ru.hokan.sharingan.common.crawler import Crawler


class ImgurCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 6
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_imgur' + os.path.sep
    __TARGET_URL = 'http://prntscr.com/'

    def __init__(self):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY)

    def _get_random_url_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))
