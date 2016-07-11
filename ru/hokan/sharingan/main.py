import logging
from optparse import OptionParser

from ru.hokan.sharingan.crawlers.ImgurCrawler import ImgurCrawler

DEFAULT_NUMBER_OF_IMAGES = 3
DEFAULT_TEXT_EXTRACTION_DECISION = False

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = OptionParser()
    parser.add_option("-n", "--number-of-images", dest="number_of_images",
                      help="number of images to grab from site")
    parser.add_option("--min-width", dest="min_width",
                      help="minimum width of image")
    parser.add_option("--max-width", dest="max_width",
                      help="maximum width of image")
    parser.add_option("--min-height", dest="min_height",
                      help="minimum height of image")
    parser.add_option("--max-height", dest="max_height",
                  help="maximum height of image")
    parser.add_option("-t", "--text", action="store_true",
                      help="should text be extracted from image via Tesseract OCR")

    (options, args) = parser.parse_args()

    if options.number_of_images is None \
            and options.min_width is None \
            and options.max_width is None \
            and options.min_height is None \
            and options.max_height is None \
            and options.text is None:
        options.number_of_images = DEFAULT_NUMBER_OF_IMAGES
        options.text = DEFAULT_TEXT_EXTRACTION_DECISION

    imgur_crawler = ImgurCrawler(options.text, options.min_width, options.max_width, options.min_height, options.max_height)
    imgur_crawler.get_pictures(options.number_of_images)
