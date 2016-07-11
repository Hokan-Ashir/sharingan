import logging

from ru.hokan.sharingan.crawlers.ImgurCrawler import ImgurCrawler

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    number_of_pictures_to_find = 100

    imgur_crawler = ImgurCrawler()
    imgur_crawler.get_pictures(number_of_pictures_to_find)
