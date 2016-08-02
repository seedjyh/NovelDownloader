__author__ = 'jiangyh'

class ChapterInfo:
    def __init__(self, url, title):
        self.__url = url
        self.__title = title

    def url(self):
        return self.__url

    def title(self):
        return self.__title
