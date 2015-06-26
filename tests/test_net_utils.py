#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/6/26'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.net_utils import NetUtils
import unittest


class TestNetUtils(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_send_mail(self):
        smtp_server = NetUtils.smtp_init(host='smtp.mailgun.org', port=587, login_name='postmaster@ez-jim.com',
                                         password='password', tls=True)
        ret = NetUtils.send_mail(smtp_server=smtp_server, sender='jimit@ez-jim.com',
                                 receivers=['james.iter.cn@gmail.com', '297362831@qq.com'], title='Test Mail',
                                 message='Hello!')

        ret = NetUtils.send_mail(smtp_server=smtp_server, sender='jimit@ez-jim.com',
                                 receivers=['james.iter.cn@gmail.com', '297362831@qq.com'], title='Test Mail',
                                 message='Hello!')
        pass
