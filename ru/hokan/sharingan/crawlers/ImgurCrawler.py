import os
import random
import string

from ru.hokan.sharingan.common.Configuration import Configuration
from ru.hokan.sharingan.common.Crawler import Crawler


class ImgurCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 6
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_imgur' + os.path.sep
    __TARGET_URL = 'http://prntscr.com/'

    def __init__(self):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY)

    def _get_random_url_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))

    def _should_image_be_processed(self, image):
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
