#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.router import Router, router_table
from jimit.ji_time import JITime
import unittest

reload(sys)
sys.setdefaultencoding('utf8')


class TestRouter(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_launcher(self):
        router_table['today'] = JITime.today
        self.assertEqual(Router.launcher(action='today', content='-'), JITime.today())


if __name__ == '__main__':
    unittest.main()
