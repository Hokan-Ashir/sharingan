from ru.hokan.sharingan.ImgurCrawler import ImgurCrawler
from ru.hokan.sharingan.PrntScrCrawler import PrntScrCrawler

if __name__ == '__main__':
    number_of_pictures_to_find = 100

    prt_scr_crawler = PrntScrCrawler()
    prt_scr_crawler.get_pictures(number_of_pictures_to_find)

    imgur_crawler = ImgurCrawler()
    imgur_crawler.get_pictures(number_of_pictures_to_find)
