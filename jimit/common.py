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
import random
import json
from state_code import *
import jimit as ji


class Common(object):

    def __init__(self):
        pass

    @staticmethod
    def exchange_state(code):
        """
        :rtype : dict
        :param code: 状态码
        :return: dict格式返回状态信息
        """
        if not isinstance(code, int):
            result = Common.exchange_state(50001)
            raise ji.JITError(json.dumps(result, ensure_ascii=False))

        trunk_code = int(code / 100)
        if str(trunk_code) not in index_state['trunk']:
            result = Common.exchange_state(50002)
            raise ji.JITError(json.dumps(result, ensure_ascii=False))

        result = copy.copy(index_state['trunk'][(str(trunk_code))])

        if str(code) in index_state['branch']:
            result['sub'] = copy.copy(index_state["branch"][(str(code))])

        return result

    @staticmethod
    def ts():
        """
        :rtype : int
        :return: 当前以秒为单位的时间戳
        """
        return int(time.time())

    @staticmethod
    def tms():
        """
        :rtype : int
        :return: 当前以毫秒为单位的时间戳
        """
        return int(time.time() * 1000)

    @staticmethod
    def tus():
        """
        :rtype : int
        :return: 当前已微妙为单位的时间戳
        """
        return int(time.time() * 1000000)

    @staticmethod
    def get_hostname():
        """
        :rtype : basestring
        :return: 主机名
        """
        return socket.gethostname()

    @staticmethod
    def get_environment(according_to_hostname=True):
        """
        :rtype : str
        :param according_to_hostname: 是否按主机名来识别环境
        :return: 当前所处环境
        """

        def exchange_env(environment_string):
            if environment_string.lower().find('debug') != -1:
                return 'debug'
            elif environment_string.lower().find('sandbox') != -1:
                return 'sandbox'
            else:
                return 'production'

        if according_to_hostname:
            environment = exchange_env(str(Common.get_hostname()))  # get_hostname返回的basestring类型没有lower方法
        else:
            environment = exchange_env(os.environ.get('JI_ENVIRONMENT', ''))

        return environment

    @staticmethod
    def calc_sha1_by_file(file_path):
        """
        :rtype : dict
        :param file_path: 欲计算其sha1 hash值的文件路径
        :return: lower格式的sha1 hash值
        """
        result = dict()
        result['state'] = Common.exchange_state(20000)

        if not os.path.isfile(file_path):
            result['state'] = Common.exchange_state(40401)
            result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                       '，目标"', file_path, '"不是一个有效文件'])
            raise ji.JITError(json.dumps(result))

        with open(file_path, 'rb') as f:
            try:
                sha1_obj = hashlib.sha1()
                sha1_obj.update(f.read())
                return sha1_obj.hexdigest()
            except Exception, e:
                result['state'] = Common.exchange_state(50004)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                           '，详细信息: ', e.message])
                raise ji.JITError(json.dumps(result))

    @staticmethod
    def calc_sha1_by_fd(fd):
        """
        :rtype : dict
        :param fd: 欲计算其sha1 hash值的文件描述符
        :return: lower格式的sha1 hash值
        """
        result = dict()
        result['state'] = Common.exchange_state(20000)

        try:
            sha1_obj = hashlib.sha1()
            sha1_obj.update(fd.read())
            sha1 = sha1_obj.hexdigest()
        except Exception, e:
            result['state'] = Common.exchange_state(50004)
            result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'],
                                                       '，详细信息: ', e.message])
            raise ji.JITError(json.dumps(result))
        finally:
            fd.seek(0, 0)

        return sha1

    @staticmethod
    def generate_random_code(length, letter_form='mix', numeral=True, spechars=False):
        """
        :rtype : dict
        :param length: 随机值长度，最长1000字符
        :param letter_form: 字母表现形式['lower'(小写) | 'upper'(大写) | 'mix'(混合)]
        :param numeral: 是否允许数字参选随机值
        :param spechars: 是否允许特殊字符参选随机值
        :return: 随机选取的字符串
        """
        args_rules = [
            (int, 'length', (1, 1000)),
            (basestring, 'letter_form', ['lower', 'upper', 'mix']),
            (bool, 'numeral'),
            (bool, 'spechars')
        ]

        ji.Check.previewing(args_rules, locals())

        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_characters = ['!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                              '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

        character_codes = []
        if letter_form == 'lower':
            character_codes.extend(lower)
        elif letter_form == 'upper':
            character_codes.extend(upper)
        elif letter_form == 'mix':
            character_codes.extend(lower)
            character_codes.extend(upper)

        if numeral:
            character_codes.extend(number)

        if spechars:
            character_codes.extend(special_characters)

        random_code = ''

        while length:
            length -= 1
            random_code = ''.join([random_code, random.choice(character_codes)])

        return random_code
