__author__ = 'jiangyh'

import unittest
from TextParser import TextParser, NoSuchKeywordException

class TestTextParser(unittest.TestCase):
    def test_JumpStr_and_GetStr(self):
        parser = TextParser('1234567')
        self.assertEqual('1234567', parser.GetStr())
        parser.SetBegin()
        self.assertEqual('234567', parser.JumpStr('1').GetStr())
        parser.SetBegin()
        self.assertEqual('23456', parser.JumpStr('1').GetStr('7'))
        parser.SetBegin()
        self.assertEqual('345', parser.JumpStr('2').GetStr('6'))
        parser.SetBegin()
        self.assertEqual('345', parser.JumpStr('1').JumpStr('2').GetStr('6'))

        parser = TextParser('abcd,abcd,abcd')
        self.assertEqual('bc', parser.JumpStr('a').GetStr('d'))
        parser.SetBegin()
        self.assertEqual(',abcd', parser.JumpStr('d').JumpStr('d').GetStr(''))
        parser.SetBegin()
        self.assertEqual(',abc', parser.JumpStr('d').JumpStr('d').GetStr('d'))
        parser.SetBegin()
        self.assertEqual(',abc', parser.JumpStr('d', 2).GetStr('d'))

    def test_GetStr_until_end(self):
        '''
        GetStr without argumnet means get string from now position to the end.
        :return:
        '''
        parser = TextParser('abcd,efgh,ijkl')
        self.assertEqual('ijkl', parser.JumpStr(',', 2).GetStr())

    def test_JumpStr_no_keyword(self):
        parser = TextParser('Hello, world')
        self.assertRaises(NoSuchKeywordException, parser.JumpStr, 'abc', 1)

    def test_JumpStr_no_enough_keyword(self):
        parser = TextParser('Hello, world')
        self.assertRaises(NoSuchKeywordException, parser.JumpStr, 'o', 3)