from ru.hokan.sharingan.crawler import crawler

if __name__ == '__main__':
    image_crawler = crawler()
    image_crawler.get_pictures(100)
