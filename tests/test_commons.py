#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit import Common
import unittest


class TestCommons(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_exchange_state(self):
        self.assertEqual('41201', Common.exchange_state(41201)['sub']['code'])

    def test_ts(self):
        import time
        self.assertEqual(int(time.time()), Common.ts())

    def test_get_hostname(self):
        import socket
        self.assertEqual(socket.gethostname(), Common.get_hostname())

    def test_get_environment(self):
        import os
        os.environ['JI_ENVIRONMENT'] = 'debug.host.com'
        self.assertEqual('debug', Common.get_environment(False))

        os.environ['JI_ENVIRONMENT'] = 'sandbox.host.com'
        self.assertEqual('sandbox', Common.get_environment(False))

        os.environ.pop('JI_ENVIRONMENT')
        self.assertEqual('production', Common.get_environment(False))

        hostname = Common.get_hostname()
        if hostname.lower().find('debug') != -1:
            self.assertEqual('debug', Common.get_environment(True))
        elif hostname.lower().find('sandbox') != -1:
            self.assertEqual('sandbox', Common.get_environment(True))
        else:
            self.assertEqual('production', Common.get_environment(True))

    def test_calc_sha1_by_file(self):
        import os, hashlib
        file_path = __file__
        sha1 = Common.calc_sha1_by_file(file_path)
        with open(file_path, 'rb') as f:
            sha1_obj = hashlib.sha1()
            sha1_obj.update(f.read())
            self.assertEqual(sha1, sha1_obj.hexdigest())

    def test_generate_random_code(self):
        ret = Common.generate_random_code(100)
        self.assertEqual(100, ret.__len__())

    """
    def test_raw_input(self):
        ret = Common.raw_input(u'请输入: ')
        self.assertIsInstance(ret, basestring)
    """

if __name__ == '__main__':
    unittest.main()
