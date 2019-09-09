#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/6/24'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.security import Security
import unittest


class TestSecurity(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ji_pbkdf2(self):
        ret = Security.ji_pbkdf2('password')
        self.assertIsInstance(ret, str)

    def test_ji_pbkdf2_check(self):
        ji_pbkdf2_ret = Security.ji_pbkdf2('password')
        ret = Security.ji_pbkdf2_check(password='password', password_hash=ji_pbkdf2_ret)
        self.assertEqual(True, ret)

    def test_ji_hash_sign(self):
        sign = Security.ji_hash_sign(algorithm='sha1', secret='cke2Ziz6rdraqj6yZoNfFGQvNSnTSeU3',
                                     content={'k1': 'v1', 'k2': 'v2'})
        self.assertEqual('e0c901d37eb51cc61feb5eaf4bda60eb21d78576', sign)

