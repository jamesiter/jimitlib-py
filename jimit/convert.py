#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import decimal

from common import *


class Convert():

    def __init__(self):
        pass

    @staticmethod
    def sql2json(sql_obj):
        j_sql = dict()
        result = dict()
        result['state'] = Common.exchange_state(20000)

        try:
            for col in sql_obj._sa_class_manager.mapper.mapped_table.columns:
                if isinstance(getattr(sql_obj, col.name), decimal.Decimal):
                    j_sql[col.name] = str(getattr(sql_obj, col.name))
                else:
                    j_sql[col.name] = getattr(sql_obj, col.name)
        except Exception, e:
            result['state'] = Common.exchange_state(50003)
            result['state']['sub']['detail'] = e.message
            return result

        result['j_sql'] = j_sql
        return result
