__author__ = 'jiangyh'

from BookPageAnalyser import BookPageAnalyser
from TextParser import TextParser, NoSuchKeywordException
from ChapterInfo import ChapterInfo
from UrlHandle import UrlHandle

class SilukeBookPageAnalyser(BookPageAnalyser):
    def __init__(self, url, pagestr):
        self.__url = url
        self.__pagestr = pagestr

    def get_book_title(self):
        parser = TextParser(self.__pagestr)
        return self.Utf8ToAnsi(parser.JumpStr('<h1>', 1).JumpStr('>', 1).GetStr('<'))

    def get_book_author(self):
        parser = TextParser(self.__pagestr)
        return self.Utf8ToAnsi(parser.JumpStr('<span>', 2).JumpStr('<strong>').GetStr('<'))

    def get_chapter_info_list(self):
        parser = TextParser(self.__GetPagePartContainsChapterInformation())
        chapter_info_list = list()
        while (True):
            try:
                relative_url = parser.JumpStr('href="').GetStr('"')
            except NoSuchKeywordException:
                break
            title = self.Utf8ToAnsi(parser.JumpStr('>').GetStr('<'))
            chapter_info_list.append(ChapterInfo(UrlHandle(self.__url).GetHost() + relative_url, title))
        return chapter_info_list

    def __GetPagePartContainsChapterInformation(self):
        parser = TextParser(self.__pagestr)
        return parser.JumpStr('class="booklist"').GetStr('</div>')