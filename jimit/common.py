#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import time
import copy
import socket
import os
import hashlib
from state_code import *


class Common():

    def __init__(self):
        pass

    @staticmethod
    def exchange_state(code):
        if not isinstance(code, int):
            result = Common.exchange_state(50001)
            return result

        trunk_code = int(code / 100)
        if str(trunk_code) not in index_state['trunk']:
            result = Common.exchange_state(50002)
            return result

        result = copy.copy(index_state['trunk'][(str(trunk_code))])

        if str(code) in index_state['branch']:
            result['sub'] = copy.copy(index_state["branch"][(str(code))])

        return result

    @staticmethod
    def ts():
        return int(time.time())

    @staticmethod
    def get_hostname():
        return socket.gethostname()

    @staticmethod
    def get_environment(according_to_hostname=True):

        def exchange_env(environment_string):
            if environment_string.lower().find('debug') != -1:
                return 'debug'
            elif environment_string.lower().find('sandbox') != -1:
                return 'sandbox'
            else:
                return 'production'

        if according_to_hostname:
            environment = exchange_env(Common.get_hostname())
        else:
            environment = exchange_env(os.environ.get('JI_ENVIRONMENT', ''))

        return environment

    @staticmethod
    def calc_sha1_by_file(file_path):
        result = dict()
        result['state'] = Common.exchange_state(20000)

        if not os.path.isfile(file_path):
            result['state'] = Common.exchange_state(40401)
            result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                       '，目标"', file_path, '"不是一个有效文件'])
            return result

        with open(file_path, 'rb') as f:
            try:
                sha1_obj = hashlib.sha1()
                sha1_obj.update(f.read())
                result['sha1'] = sha1_obj.hexdigest()
            except Exception, e:
                result['state'] = Common.exchange_state(50004)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                           '，详细信息: ', e.message])
                return result

        return result

    @staticmethod
    def calc_sha1_by_fd(fd):
        result = dict()
        result['state'] = Common.exchange_state(20000)

        try:
            sha1_obj = hashlib.sha1()
            sha1_obj.update(fd.read())
            result['sha1'] = sha1_obj.hexdigest()
        except Exception, e:
            result['state'] = Common.exchange_state(50004)
            result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                       '，详细信息: ', e.message])
            return result
        finally:
            fd.seek(0, 0)

        return result
