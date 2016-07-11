import os
import random
import string

from ru.hokan.sharingan.common.crawler import Crawler


class ImgurCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 6
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_imgur' + os.path.sep
    __TARGET_URL = 'http://prntscr.com/'
    __minimum_width = None
    __maximum_width = None
    __minimum_height = None
    __maximum_height = None

    def __init__(self, should_extract_text, minimum_width, maximum_width, minimum_height, maximum_height):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY, should_extract_text)
        self.__minimum_width = minimum_width
        self.__maximum_width = maximum_width
        self.__minimum_height = minimum_height
        self.__maximum_height = maximum_height

    def _get_random_url_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))

    def _should_image_be_processed(self, image):
        width, height = image.size
        min_width_passed = True if self.__minimum_width is None else height >= self.__minimum_width
        max_width_passed = True if self.__maximum_width is None else width <= self.__maximum_width
        min_height_passed = True if self.__minimum_height is None else height >= self.__minimum_height
        max_height_passed = True if self.__maximum_height is None else height <= self.__maximum_height

        return min_width_passed and max_width_passed and min_height_passed and max_height_passed
