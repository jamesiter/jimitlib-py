#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.append("..")
from jimit.terminal.color import Color
import unittest


__author__ = 'James Iter'
__date__ = '16/6/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class TestColor(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_error(self):
        print Color.error(u'错误')

    def test_error_blink(self):
        print Color.error_blink(u'错误')

    def test_warning(self):
        print Color.warning(u'警告')

    def test_warning_blink(self):
        print Color.warning_blink(u'警告')

    def test_succeed(self):
        print Color.succeed(u'成功')

    def test_succeed_blink(self):
        print Color.succeed_blink(u'成功')


if __name__ == '__main__':
    unittest.main()
