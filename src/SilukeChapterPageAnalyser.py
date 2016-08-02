__author__ = 'jiangyh'

from ChapterPageAnalyser import ChapterPageAnalyser
from TextParser import TextParser

class SilukeChapterPageAnalyser(ChapterPageAnalyser):
    def __init__(self, pagestr):
        self.__pagestr = pagestr

    def get_chapter_title(self):
        parser = TextParser(self.__pagestr)
        return parser.JumpStr('keywords').JumpStr('content="').GetStr('"').decode('utf-8').encode('gbk')

    def get_content(self):
        parser = TextParser(self.__pagestr)
        return parser.JumpStr('"cont"').JumpStr('<br>').GetStr('<script').decode('utf-8').encode('gbk').replace('<br>', '\n')
