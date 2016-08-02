#!/usr/bin/python
# -*- coding: gbk -*-
__auther__ = 'jiangyh'

import unittest
from SilukeMainPageAnalyser import SilukeMainPageAnalyser

class TestSilukeMainPageAnalyser(unittest.TestCase):
    def setUp(self):
        self.__pagestr = self.__LoadFile('test_data/siluke_main_page.html')
        pass

    def test_get_book_title(self):
        analyser = SilukeMainPageAnalyser()
        self.assertEqual('全职高手', analyser.get_book_title(self.__pagestr))

    def test_get_book_auther(self):
        analyser = SilukeMainPageAnalyser()
        self.assertEqual('蝴蝶蓝', analyser.get_book_title(self.__pagestr))

    def test_get_chapter_info_list(self):
        analyser = SilukeMainPageAnalyser()
        info_list = analyser.get_chapter_info_list(self.__pagestr)
        self.assertEqual(1734, len(info_list))

    def __LoadFile(self, file_name):
        file_object = open(file_name, 'rb')
        data = file_object.read()
        file_object.close()
        return data


