import os
import random
import string

from ru.hokan.sharingan.crawler import Crawler


class PrntScrCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 32
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_prntscr' + os.path.sep
    __TARGET_URL = 'http://image.prntscr.com/image/'

    def __init__(self):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY)

    def _get_random_image_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))
