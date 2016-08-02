__author__ = 'jiangyh'

class NoSuchKeywordException:
    def __init__(self, keyword):
        self.__keyword = keyword

class TextParser:
    def __init__(self, text):
        self.__text = text
        self.__now_pos = 0

    def SetBegin(self):
        self.__now_pos = 0

    def JumpStr(self, keyword, count=1):
        for i in range(count):
            keyword_pos = self.__text.find(keyword, self.__now_pos)
            if keyword_pos == -1:
                raise NoSuchKeywordException(keyword)
            else:
                self.__now_pos = keyword_pos + len(keyword)
        return self

    def GetStr(self, termchar=''):
        end_pos = len(self.__text)
        if termchar != '':
            keyword_pos = self.__text.find(termchar, self.__now_pos)
            if keyword_pos != -1:
                end_pos = keyword_pos
        return self.__text[self.__now_pos:end_pos]
