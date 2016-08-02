__author__ = 'jiangyh'

class UrlHandle:
    def __init__(self, url):
        self.__url = url

    def GetHost(self):
        now_pos = self.__url.find('//') + len('//')
        now_pos = self.__url.find('/', now_pos)
        return self.__url[:now_pos]
