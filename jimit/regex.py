#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'James Iter'
__date__ = '2017/3/21'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


class Regex(object):

    @staticmethod
    def ip():
        return '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'

    @staticmethod
    def email():
        return '^[a-z0-9]{1,20}([._][a-z0-9]{1,20}){0,5}@[a-z0-9]{1,20}([-][a-z0-9]{1,20}){0,2}\.[a-z]{1,5}$'

