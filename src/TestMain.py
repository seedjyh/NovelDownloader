__auther__ = 'jiangyh'

'''
Running this file means running all test cases in this project.
'''

import unittest
from TestSilukeBookPageAnalyser import TestSilukeBookPageAnalyser
from TestTextParser import TestTextParser
from TestChapterInfo import TestChapterInfo
from TestUrlHandle import TestUrlHandle
from TestSilukeChapterPageAnalyser import TestSilukeChapterPageAnalyser

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestTextParser('test_JumpStr_and_GetStr'))
    suite.addTest(TestTextParser('test_GetStr_until_end'))
    suite.addTest(TestTextParser('test_JumpStr_no_keyword'))
    suite.addTest(TestTextParser('test_JumpStr_no_enough_keyword'))

    suite.addTest(TestChapterInfo('test_init_url_title'))

    suite.addTest(TestUrlHandle('test_GetHost'))

    suite.addTest(TestSilukeBookPageAnalyser('test_get_book_title'))
    suite.addTest(TestSilukeBookPageAnalyser('test_get_book_author'))
    suite.addTest(TestSilukeBookPageAnalyser('test_get_chapter_info_list'))

    suite.addTest(TestSilukeChapterPageAnalyser('test_get_chapter_title'))
    suite.addTest(TestSilukeChapterPageAnalyser('test_get_content'))

    unittest.TextTestRunner(verbosity=2).run(suite)
