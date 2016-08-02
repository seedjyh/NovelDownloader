__auther__ = 'jiangyh'

'''
Running this file means running all test cases in this project.
'''

import unittest
from TestSilukeMainPageAnalyser import TestSilukeMainPageAnalyser

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSilukeMainPageAnalyser('test_get_book_title'))
    suite.addTest(TestSilukeMainPageAnalyser('test_get_book_auther'))
    suite.addTest(TestSilukeMainPageAnalyser('test_get_chapter_info_list'))
    unittest.TextTestRunner(verbosity=2).run(suite)
