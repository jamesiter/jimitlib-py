#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.commons import Commons
import unittest


class TestCommons(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_exchange_state(self):
        self.assertEqual('41201', Commons.exchange_state(41201)['sub']['code'])

    def test_ts(self):
        import time
        self.assertEqual(int(time.time()), Commons.ts())


if __name__ == '__main__':
    unittest.main()