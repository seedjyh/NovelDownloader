__author__ = 'jiangyh'


import urllib
import urllib2
from Book import Book
from Chapter import Chapter
from SilukeBookPageAnalyser import SilukeBookPageAnalyser
from SilukeChapterPageAnalyser import SilukeChapterPageAnalyser
from TextParser import NoSuchKeywordException

class SilukeNovelDownloader:
    def DownloadBook(self, url):
        book_page_analyser = SilukeBookPageAnalyser(url, self.__DownloadUrl(url))
        chapter_list = [self.DownloadChapter(chapter_info.url()) for chapter_info in book_page_analyser.get_chapter_info_list()]

        return Book(
            book_page_analyser.get_book_title(),
            book_page_analyser.get_book_author(),
            chapter_list
        )

    def DownloadChapter(self, url):
        print('downloading chapter: ' + url)
        chapter_page_analyser = SilukeChapterPageAnalyser(self.__DownloadUrl(url))
        try:
            chapter =  Chapter(
                chapter_page_analyser.get_chapter_title(),
                chapter_page_analyser.get_content()
            )
            print('download OK, tilte=%s, length=%d'%(chapter.title(), len(chapter.content())))
        except NoSuchKeywordException:
            print(url)
        return chapter

    def __DownloadUrl(self, url):
        while (True):
            try:
                req = urllib2.Request(url)
                f = urllib2.urlopen(req)
                pagestr = f.read()
                f.close()
                break
            except urllib2.HTTPError:
                continue
        return pagestr
