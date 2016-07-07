import logging
import os
import random
import string
import urllib2

from ru.hokan.sharingan.common.crawler import Crawler


class PrntScrCrawler(Crawler):
    __IMAGE_NAME_LENGTH = 32
    __OUTPUT_DIRECTORY = '.' + os.path.sep + 'output_prntscr' + os.path.sep
    __TARGET_URL = 'http://image.prntscr.com/image/'

    def __init__(self):
        Crawler.__init__(self, self.__TARGET_URL, self.__OUTPUT_DIRECTORY)

    def _get_random_image_name(self):
        return ''.join(random.choice(string.lowercase + string.digits) for i in range(self.__IMAGE_NAME_LENGTH))

    def _should_image_be_processed(self, full_image_url):
        try:
            req = urllib2.Request(full_image_url, None, {
                'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            logging.debug('Failed to filter url: ' + full_image_url + ' reason: ' + str(e.getcode()))
            return False

        return True
