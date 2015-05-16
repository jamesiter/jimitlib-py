#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.ji_time import JITime
import unittest
import time


class TestJITime(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gmt(self):
        self.assertEqual(time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()), JITime.gmt())

    def test_today(self):
        self.assertEqual(time.strftime('%Y-%m-%d'), JITime.today())

    def test_now_time(self):
        self.assertEqual(time.strftime('%H:%M:%S'), JITime.now_time())

    def test_now_date_time(self):
        self.assertEqual(time.strftime('%Y-%m-%d %H:%M:%S'), JITime.now_date_time())

    def test_week(self):
        self.assertEqual(time.strftime('%W'), JITime.week())


if __name__ == '__main__':
    unittest.main()
