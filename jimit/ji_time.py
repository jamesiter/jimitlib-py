#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from common import *
import datetime


class JITime(object):
    """
    力图简单、直接，故把常用时间输出封装为静态函数
    """

    def __init__(self):
        pass

    @staticmethod
    def gmt(ts=Common.ts()):
        """
        :rtype : str
        :param ts: 指定时间戳，默认系统当前时间戳
        :return: GMT格式的当前时间('Thu, 18 Jun 2015 10:06:28 GMT')
        """
        return time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(ts))

    @staticmethod
    def today(separator='-'):
        """
        :rtype : str
        :param separator: 年、月、日之间的间隔符，默认为'-'
        :return: 当天日期('2015-06-18')
        """
        fmt = separator.join(['%Y', '%m', '%d'])
        return time.strftime(fmt)

    @staticmethod
    def now_time(separator=':'):
        """
        :rtype : str
        :param separator: 时、分、秒之间的间隔符，默认为':'
        :return: 当前系统的时间('18:08:28')
        """
        fmt = separator.join(['%H', '%M', '%S'])
        return time.strftime(fmt)

    @staticmethod
    def now_date_time(date_separator='-', time_separator=':', dt_separator=' '):
        """
        :rtype : str
        :param date_separator: 日期年、月、日之间的间隔符，默认为'-'
        :param time_separator: 时间时、分、秒之间的间隔符，默认为':'
        :param dt_separator: 日期与时间之间的间隔符，默认为' '
        :return: 当前系统的日期时间('2015-06-18 18:12:04')
        """
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
        """
        :rtype : str
        :param offset: 以日为单位，向前偏移n值的日期
        :param separator: 日期年、月、日之间的分隔符，默认为'-'
        :return: 向前偏移n日的日期(jimit.JITime.the_day_before_today(20) --> '2015-05-29')
        """
        return JITime.the_day(datetime.date.today() - datetime.timedelta(days=offset), separator)

    @staticmethod
    def the_day_after_today(offset=0, separator='-'):
        """
        :rtype : str
        :param offset: 以日为单位，向后偏移n值的日期
        :param separator: 日期年、月、日之间的间隔符，默认值'-'
        :return: 向后偏移n日的日期(jimit.JITime.the_day_after_today(20) --> '2015-07-08')
        """
        return JITime.the_day(datetime.date.today() + datetime.timedelta(days=offset), separator)

    @staticmethod
    def the_month_before_this_month_ts(offset=0):
        """
        :rtype : int
        :param offset: 以月为单位，像前偏移n值的月期
        :return: 像前偏移n月的月初时间戳
        """
        today_date = datetime.date.today()
        offset_year = offset / 12
        offset_month = offset % 12
        if today_date.month == offset_month:
            offset_month -= 12
            offset_year += 1
        return int(today_date.replace(year=today_date.year - offset_year, month=today_date.month - offset_month,
                                      day=1).strftime('%s'))

    @staticmethod
    def the_month_after_this_month_ts(offset=0):
        """
        :rtype : int
        :param offset: 以月为单位，像后偏移n值的月期
        :return: 像后偏移n月的月初时间戳
        """
        today_date = datetime.date.today()
        offset += today_date.month
        offset_year = offset / 12
        offset_month = offset % 12
        return int(today_date.replace(year=today_date.year + offset_year, month=offset_month,
                                      day=1).strftime('%s'))

    @staticmethod
    def week():
        """
        :rtype : str
        :return: 当前系统时间所在当年的周期('24')
        """
        return time.strftime('%W')
