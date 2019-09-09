#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .common import *
import hashlib


__author__ = 'James Iter'
__date__ = '15/6/24'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


class Security(object):

    @staticmethod
    def ji_pbkdf2(password='', quality=1000, algorithm='sha1', salt=''):
        """ jimit pbkdf2的实现
        :rtype: dict
        :param password: 输入的密码
        :param quality: 质量(复杂度，即循环执行散列算法多少次，默认1000)
        :param algorithm: 散列算法，支持的有['md5', 'sha1', 'sha256', 'sha512']，默认是sha1
        :param salt: 可以自定义salt，如果不指定，将产生默认32字符的salt，该参数主要用于ji_pbkdf2_check
        :return: 返回字典中password_hash为生成的秘密
        """
        password_length = password.__len__()
        args_rules = [
            (str, 'password'),
            (int, 'quality', (1, 10000)),
            (str, 'algorithm', ['md5', 'sha1', 'sha256', 'sha512']),
            (int, 'password_length', (0, 1024)),
            (str, 'salt')
        ]

        ji.Check.previewing(args_rules, locals())

        if salt == '':
            salt = Common.generate_random_code(length=32)
        else:
            salt = salt

        password_hash = ''.join([salt, password])
        hash_method = None
        if algorithm == 'md5':
            hash_method = hashlib.md5
        elif algorithm == 'sha1':
            hash_method = hashlib.sha1
        elif algorithm == 'sha256':
            hash_method = hashlib.sha256
        elif algorithm == 'sha512':
            hash_method = hashlib.sha512
        else:
            raise KeyError(''.join(['Not support algorithm: ', algorithm]))

        tmp_quality = quality
        while tmp_quality:
            password_hash = hash_method(password_hash.encode('utf-8')).hexdigest()
            tmp_quality -= 1

        return '$'.join(['ji_pbkdf2', algorithm, str(quality), salt, password_hash])

    @staticmethod
    def ji_pbkdf2_check(password='', password_hash=''):
        """ 校验密码
        :rtype : dict
        :param password: 原始密码
        :param password_hash: 比对的密码hash字符串
        :return: 返回的字典中没有auth_pass key或auth_pass为False都为校验失败，只有auth_pass为True时才为校验通过
        """
        password_hash_segment = password_hash.split('$')
        password_hash_segment_length = password_hash_segment.__len__()
        args_rules = [
            (str, 'password'),
            (str, 'password_hash'),
            (int, 'password_hash_segment_length', [5])
        ]

        ji.Check.previewing(args_rules, locals())

        method = password_hash_segment[0]
        algorithm = password_hash_segment[1]
        quality = int(password_hash_segment[2])
        salt = password_hash_segment[3]

        if password_hash == Security.ji_pbkdf2(password=password, quality=quality, algorithm=algorithm, salt=salt):
            return True

        return False

    @staticmethod
    def ji_hash_sign(algorithm='sha1', secret='', content=None):
        """ 生成哈希签名
        :param algorithm: 计算签名的哈希算法,支持有md5、sha1、sha256、sha512
        :param secret: 签名用的安全码
        :param content: 计算签名的内容
        :return: 返回签名
        """
        args_rules = [
            (str, 'algorithm', ['md5', 'sha1', 'sha256', 'sha512']),
            (str, 'secret'),
            (dict, 'content', (1, 1024))
        ]

        ji.Check.previewing(args_rules, locals())

        v_list = list()
        for k in sorted(content.keys()):
            if 0 == content[k].__str__().__len__():
                continue

            v_list.append('='.join([k.__str__(), content[k].__str__()]))

        v_list.append('='.join(['secret', secret]))
        ligature = '&'.join(v_list)

        hash_method = None
        if algorithm == 'md5':
            hash_method = hashlib.md5
        elif algorithm == 'sha1':
            hash_method = hashlib.sha1
        elif algorithm == 'sha256':
            hash_method = hashlib.sha256
        elif algorithm == 'sha512':
            hash_method = hashlib.sha512
        else:
            raise KeyError(''.join(['Not support algorithm: ', algorithm]))

        return hash_method(ligature.encode('utf-8')).hexdigest()

