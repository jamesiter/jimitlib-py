#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '16/1/24'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


import time
import sys
sys.path.append("..")
from jimit.transaction_serial_number import TransactionSerialNumber
import unittest


class TestTransactionSerialNumber(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionSerialNumber(self):
        tsn = TransactionSerialNumber()
        tsn.launch()
        # while True:
        #     print tsn.generate_tsn()
        #     time.sleep(0.01)

if __name__ == '__main__':
    unittest.main()
