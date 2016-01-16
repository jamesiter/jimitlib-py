#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '16/1/17'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.keep_read import KeepRead
import unittest


@staticmethod
def filtrator(line=None):
    print line


class TestKeepRead(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testKeepRead(self):
        KeepRead.filtrator = filtrator
        # KeepRead.launch()


if __name__ == '__main__':
    unittest.main()
