import os
import random
import string

from ru.hokan.sharingan.common.crawler import Crawler


class PrntScrCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 6
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_prntscr' + os.path.sep
    __TARGET_URL = 'http://prntscr.com/'

    def __init__(self, should_text_be_extracted):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY, should_text_be_extracted)

    def _get_random_url_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))

    def _get_image_url_from_source(self, url_data):
        data = url_data.read()
        url_data.close()
        return str(data).split("ifr.registerMainWindow(")[1].split(",")[0].replace("\"", "")