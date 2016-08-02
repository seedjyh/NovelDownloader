#!/usr/bin/python
# -*- coding: gbk -*-
__author__ = 'jiangyh'

import unittest
from PageAnalyser import PageAnalyser

class TestPageAnalyser(unittest.TestCase):
    def test_Utf8ToAnsi(self):
        self.assertEqual('测试', PageAnalyser().Utf8ToAnsi('\xE6\xB5\x8B\xE8\xAF\x95'))
        self.assertEqual('测试', PageAnalyser().Utf8ToAnsi('\xE6\xB5\x8B\xE2\x80\xA2\xE8\xAF\x95'))
