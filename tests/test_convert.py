#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/7/12'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from jimit.convert import Convert
import unittest


class TestConvert(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dumps(self):

        @Convert.dumps
        def tmp_fun():
            return {'OK': True}

        self.assertEqual('{"OK": true}', tmp_fun())

if __name__ == '__main__':
    unittest.main()
