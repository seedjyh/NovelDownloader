__author__ = 'jiangyh'

from ChapterPageAnalyser import ChapterPageAnalyser
from TextParser import *

class SilukeChapterPageAnalyser(ChapterPageAnalyser):
    def __init__(self, pagestr):
        self.__pagestr = pagestr

    def get_chapter_title(self):
        parser = TextParser(self.__pagestr)
        return self.Utf8ToAnsi(parser.JumpStr('keywords').JumpStr('content="').GetStr('"'))

    def get_content(self):
        parser = TextParser(self.__pagestr)
        return self.Utf8ToAnsi(parser.JumpStr('"cont"').GetStr('<script')).replace('<br>', '\n').replace('<br/>', '\n')
