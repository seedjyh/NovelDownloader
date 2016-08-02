__author__ = 'jiangyh'

import unittest
from UrlHandle import UrlHandle

class TestUrlHandle(unittest.TestCase):
    def test_GetHost(self):
        handle = UrlHandle('http://www.cnblogs.com/dkblog/archive/2011/06/24/2089026.html')
        self.assertEqual('http://www.cnblogs.com', handle.GetHost())

