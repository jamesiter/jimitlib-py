#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .common import *
import json
import decimal


__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


class Convert(object):

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
        except Exception as e:
            result['state'] = Common.exchange_state(50003)
            result['state']['sub']['detail'] = e.__str__()
            raise ji.JITError(json.dumps(result))

        result['j_sql'] = j_sql
        return result['j_sql']

    @staticmethod
    def dumps(func):
        def _dumps(*args, **kwargs):
            ret = func(*args, **kwargs)
            return json.dumps(ret, ensure_ascii=False)
        return _dumps
