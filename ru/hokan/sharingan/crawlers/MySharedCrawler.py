import os
import random

from ru.hokan.sharingan.common.crawler import Crawler


class MySharedScrCrawler(Crawler):
    __FIRST_URL_NUMBER_PART_LENGTH = 2
    __SECOND_URL_NUMBER_PART_LENGTH = 7
    __THIRD_URL_NUMBER_PART_LENGTH = 2
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_myshared' + os.path.sep
    __TARGET_URL = 'http://player.myshared.ru/'

    def __init__(self, should_text_be_extracted):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY, should_text_be_extracted)

    def _get_random_url_name(self):
        return str(random.randint(0, 10 ** self.__FIRST_URL_NUMBER_PART_LENGTH)) \
               + "/" \
               + str(random.randint(0, 10 ** self.__SECOND_URL_NUMBER_PART_LENGTH)) \
               + "/data/images/img" \
               + str(random.randint(0, 10 ** self.__THIRD_URL_NUMBER_PART_LENGTH)) \
               + ".jpg"

    def _get_image_url_from_source(self, url_data):
        return url_data.url