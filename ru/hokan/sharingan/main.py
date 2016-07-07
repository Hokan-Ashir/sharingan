import logging

from ru.hokan.sharingan.crawlers.ImgurCrawler import ImgurCrawler
from ru.hokan.sharingan.crawlers.PrntScrCrawler import PrntScrCrawler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    number_of_pictures_to_find = 100

    prt_scr_crawler = PrntScrCrawler()
    prt_scr_crawler.get_pictures(number_of_pictures_to_find)

    imgur_crawler = ImgurCrawler()
    imgur_crawler.get_pictures(number_of_pictures_to_find)
