#!/usr/bin/python
# -*- coding: gbk -*-
__author__ = 'jiangyh'

import unittest
from SilukeChapterPageAnalyser import SilukeChapterPageAnalyser
from FileTool import FileTool

class TestSilukeChapterPageAnalyser(unittest.TestCase):
    def setUp(self):
        self.__pagestr = FileTool().LoadFile('test_data/siluke_chapter_page.html')

    def test_get_chapter_title(self):
        analyser = SilukeChapterPageAnalyser(self.__pagestr)
        self.assertEqual('第一章 被驱逐的高手', analyser.get_chapter_title())

    def test_get_content(self):
        analyser = SilukeChapterPageAnalyser(self.__pagestr)
        content = analyser.get_content()
        self.assertEqual(8367, len(content))
        self.assertEqual('　　“卡卡卡，嗒嗒……”\n', content[:25])
