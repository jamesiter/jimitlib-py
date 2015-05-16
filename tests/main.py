#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/17'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import tests
import unittest


if __name__ == '__main__':
    suite = tests.load_tests(unittest.TestLoader(), unittest.TestSuite())
    unittest.TextTestRunner(verbosity=2).run(suite)
