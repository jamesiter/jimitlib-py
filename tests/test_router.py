#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.router import Router, router_table
import unittest
import time

reload(sys)
sys.setdefaultencoding('utf8')


router_table['ts'] = time.time


class TestRouter(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_launcher(self):
        Router.launcher(action='s')
        self.assertEqual(0, 0)
