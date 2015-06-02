#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from common import *
import datetime


class JITime():

    def __init__(self):
        pass

    @staticmethod
    def gmt(ts=Common.ts()):
        return time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(ts))

    @staticmethod
    def today(separator='-'):
        fmt = separator.join(['%Y', '%m', '%d'])
        return time.strftime(fmt)

    @staticmethod
    def now_time(separator=':'):
        fmt = separator.join(['%H', '%M', '%S'])
        return time.strftime(fmt)

    @staticmethod
    def now_date_time(date_separator='-', time_separator=':', dt_separator=' '):
        fmt = dt_separator.join([date_separator.join(['%Y', '%m', '%d']), time_separator.join(['%H', '%M', '%S'])])
        return time.strftime(fmt)

    @staticmethod
    def the_day(the_day, separator='-'):
        fmt = separator.join(['%Y', '%m', '%d'])

        if not isinstance(the_day, datetime.date):
            raise TypeError('only datetime.date')

        return the_day.strftime(fmt)

    @staticmethod
    def the_day_before_today(offset=0, separator='-'):
        return JITime.the_day(datetime.date.today()-datetime.timedelta(days=offset), separator)

    @staticmethod
    def the_day_after_today(offset=0, separator='-'):
        return JITime.the_day(datetime.date.today()+datetime.timedelta(days=offset), separator)

    @staticmethod
    def week():
        return time.strftime('%W')
