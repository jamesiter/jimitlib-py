#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/20'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import os
import json
import copy
import decimal

try:
    file_path = os.path.join(os.path.dirname(__file__), 'state_code.json')
    with open(file_path) as f:
        index_state = json.load(f)
except Exception, e:
    print e.message
    exit()


class Utils():

    def __init__(self):
        pass

    @staticmethod
    def exchange_state(code):
        if not isinstance(code, int):
            result = Utils.exchange_state(50001)
            return result

        trunk_code = int(code / 100)

        result = copy.copy(index_state['trunk'][(str(trunk_code))])

        if str(code) in index_state['branch']:
            result['sub'] = copy.copy(index_state["branch"][(str(code))])

        return result

    @staticmethod
    def previewing(member=list(), set_=dict()):
        result = dict()
        result['state'] = Utils.exchange_state(20000)

        for item in member:
            if item not in set_:
                result['state'] = Utils.exchange_state(41201)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], item])
                return result

        return result

    @staticmethod
    def sql2json(sql_obj):
        j_sql = dict()
        result = dict()
        result['state'] = Utils.exchange_state(20000)

        try:
            for col in sql_obj._sa_class_manager.mapper.mapped_table.columns:
                if isinstance(getattr(sql_obj, col.name), decimal.Decimal):
                    j_sql[col.name] = str(getattr(sql_obj, col.name))
                else:
                    j_sql[col.name] = getattr(sql_obj, col.name)
        except Exception, e:
            result['state'] = Utils.exchange_state(50002)
            result['state']['sub']['detail'] = e.message
            return result

        result['j_sql'] = j_sql
        return result
