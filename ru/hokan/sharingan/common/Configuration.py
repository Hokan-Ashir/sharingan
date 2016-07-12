class Configuration(object):
    __instance = None
    __number_of_threads = None
    __number_of_images = None
    __min_width = None
    __max_width = None
    __min_height = None
    __max_height = None
    __should_text_be_extracted = None

    def __new__(cls):
        if Configuration.__instance is None:
            Configuration.__instance = object.__new__(cls)
        return Configuration.__instance

    def set_number_of_threads(self, number_of_threads):
        self.__number_of_threads = number_of_threads

    def set_number_of_images(self, number_of_images):
        self.__number_of_images = number_of_images

    def set_min_width(self, min_width):
        self.__min_width = min_width

    def set_max_width(self, max_width):
        self.__max_width = max_width

    def set_min_height(self, min_height):
        self.__min_height = min_height

    def set_max_height(self, max_height):
        self.__max_height = max_height

    def set_should_text_be_extracted(self, should_text_be_extracted):
        self.__should_text_be_extracted = should_text_be_extracted

    def get_number_of_threads(self):
        return self.__number_of_threads

    def get_number_of_images(self):
        return self.__number_of_images

    def get_min_width(self):
        return self.__min_width

    def get_max_width(self):
        return self.__max_width

    def get_min_height(self):
        return self.__min_height

    def get_max_height(self):
        return self.__max_height

    def should_text_be_extracted(self):
        return self.__should_text_be_extracted
