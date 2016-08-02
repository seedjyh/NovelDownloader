__author__ = 'jiangyh'

from BookPageAnalyser import BookPageAnalyser
from TextParser import TextParser, NoSuchKeywordException
from ChapterInfo import ChapterInfo
from UrlHandle import UrlHandle

class SilukeBookPageAnalyser(BookPageAnalyser):
    def get_book_title(self, pagestr):
        parser = TextParser(pagestr)
        return parser.JumpStr('<h1>', 1).JumpStr('>', 1).GetStr('<').decode('utf-8').encode('gbk')

    def get_book_author(self, pagestr):
        parser = TextParser(pagestr)
        return parser.JumpStr('<span>', 2).JumpStr('<strong>').GetStr('<').decode('utf-8').encode('gbk')

    def get_chapter_info_list(self, url, pagestr):
        parser = TextParser(self.__GetPagePartContainsChapterInformation(pagestr))
        chapter_info_list = list()
        while (True):
            try:
                relative_url = parser.JumpStr('href="').GetStr('"')
            except NoSuchKeywordException:
                break
            title = parser.JumpStr('>').GetStr('<').decode('utf-8').encode('gbk')
            chapter_info_list.append(ChapterInfo(UrlHandle(url).GetHost() + relative_url, title))
        return chapter_info_list

    def __GetPagePartContainsChapterInformation(self, pagestr):
        parser = TextParser(pagestr)
        return parser.JumpStr('class="booklist"').GetStr('</div>')