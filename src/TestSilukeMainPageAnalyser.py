#!/usr/bin/python
# -*- coding: gbk -*-
__auther__ = 'jiangyh'

import unittest
from SilukeMainPageAnalyser import SilukeMainPageAnalyser

class TestSilukeMainPageAnalyser(unittest.TestCase):
    def setUp(self):
        self.__url = 'http://www.siluke.tw/ny10354/'
        self.__pagestr = self.__LoadFile('test_data/siluke_main_page.html')
        pass

    def test_get_book_title(self):
        analyser = SilukeMainPageAnalyser()
        self.assertEqual('全职高手', analyser.get_book_title(self.__pagestr))

    def test_get_book_author(self):
        analyser = SilukeMainPageAnalyser()
        self.assertEqual('蝴蝶蓝', analyser.get_book_author(self.__pagestr))

    def test_get_chapter_info_list(self):
        analyser = SilukeMainPageAnalyser()
        info_list = analyser.get_chapter_info_list(self.__url, self.__pagestr)
        self.assertEqual(1781, len(info_list))
        self.assertEqual('http://www.siluke.tw/ny10354/6071434.html', info_list[0].url())
        self.assertEqual('http://www.siluke.tw/ny10354/6071435.html', info_list[1].url())
        self.assertEqual('第一章 被驱逐的高手(文)', info_list[5].title())

    def __LoadFile(self, file_name):
        file_object = open(file_name, 'rb')
        data = file_object.read()
        file_object.close()
        return data


