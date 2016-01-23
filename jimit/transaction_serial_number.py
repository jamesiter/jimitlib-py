#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '16/1/24'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


import time
import uuid
import os
import thread
from jimit import JITime


class TransactionSerialNumber(object):

    def __init__(self):
        # YYYYMMDDHHmmSS
        self.date_time = JITime.now_date_time(date_separator='', time_separator='', dt_separator='')
        # MAC 地址的后两段的十进制值, 如 ff:ff 为 65535
        self.mac_number = '{:05d}'.format(int(uuid.uuid1().__str__()[32:], 16))
        self.pid = '{:05d}'.format(os.getpid())
        self.tsn_counter = 0

    def increment_tsn_counter(self, number=1):
        self.tsn_counter += number

    # clicking 滴答,如演奏的拍子一样
    def clicking(self):
        self.date_time = JITime.now_date_time(date_separator='', time_separator='', dt_separator='')
        self.tsn_counter = 0

    def generate_tsn(self, separator=''):
        self.increment_tsn_counter(1)
        return separator.join([self.date_time, self.mac_number, self.pid, '{:05d}'.format(self.tsn_counter)])

    def watch_tsn(self):
        while True:
            time.sleep(1)
            self.clicking()

    def launch(self):
        thread.start_new_thread(self.watch_tsn, ())
