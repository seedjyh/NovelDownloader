__author__ = 'jiangyh'

class Chapter:
    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def title(self):
        return self.__title

    def content(self):
        return self.__content
