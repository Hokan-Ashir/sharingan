import logging
from optparse import OptionParser

from ru.hokan.sharingan.common.Configuration import Configuration
from ru.hokan.sharingan.crawlers.ImgurCrawler import ImgurCrawler

DEFAULT_NUMBER_OF_IMAGES = 3
DEFAULT_TEXT_EXTRACTION_POLICY = False
DEFAULT_NUMBER_OF_THREADS = 10


def create_configuration(parsed_options):
    configuration = Configuration()
    if parsed_options.number_of_images is not None:
        configuration.set_number_of_images(parsed_options.number_of_images)
    else:
        configuration.set_number_of_images(DEFAULT_NUMBER_OF_IMAGES)

    if parsed_options.number_of_threads is not None:
        configuration.set_number_of_threads(parsed_options.number_of_threads)
    else:
        configuration.set_number_of_threads(DEFAULT_NUMBER_OF_THREADS)

    if parsed_options.min_width is not None:
        configuration.set_min_width(parsed_options.min_width)

    if parsed_options.max_width is not None:
        configuration.set_min_width(parsed_options.max_width)

    if parsed_options.min_height is not None:
        configuration.set_min_width(parsed_options.min_height)

    if parsed_options.max_height is not None:
        configuration.set_min_width(parsed_options.max_height)

    if parsed_options.should_text_be_extracted is not None:
        configuration.set_min_width(parsed_options.should_text_be_extracted)
    else:
        configuration.set_should_text_be_extracted(DEFAULT_TEXT_EXTRACTION_POLICY)


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
    parser.add_option("-t", "--threads", dest="number_of_threads",
                      help="number of threads to use")
    parser.add_option("-r", "--recognize-text", action="store_true", dest="should_text_be_extracted",
                      help="should text be extracted from image via Tesseract OCR")

    (options, args) = parser.parse_args()

    create_configuration(options)

    configuration = Configuration()
    imgur_crawler = ImgurCrawler()
    imgur_crawler.get_pictures(configuration.get_number_of_images())
