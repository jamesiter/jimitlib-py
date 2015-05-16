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

    def test_get_hostname(self):
        import socket
        self.assertEqual(socket.gethostname(), Commons.get_hostname())

    def test_get_environment(self):
        import os
        os.environ['JI_ENVIRONMENT'] = 'debug.host.com'
        self.assertEqual('debug', Commons.get_environment(False))

        os.environ['JI_ENVIRONMENT'] = 'sandbox.host.com'
        self.assertEqual('sandbox', Commons.get_environment(False))

        os.environ.pop('JI_ENVIRONMENT')
        self.assertEqual('production', Commons.get_environment(False))

        hostname = Commons.get_hostname()
        if hostname.lower().find('debug') != -1:
            self.assertEqual('debug', Commons.get_environment(True))
        elif hostname.lower().find('sandbox') != -1:
            self.assertEqual('sandbox', Commons.get_environment(True))
        else:
            self.assertEqual('production', Commons.get_environment(True))


if __name__ == '__main__':
    unittest.main()