__author__ = 'jiangyh'

import unittest
from ChapterInfo import ChapterInfo

class TestChapterInfo(unittest.TestCase):
    def test_init_url_title(self):
        info = ChapterInfo('a', 'b')
        self.assertEqual('a', info.url())
        self.assertEqual('b', info.title())
