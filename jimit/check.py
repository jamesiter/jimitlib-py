#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from common import *


class Check():

    def __init__(self):
        pass

    @staticmethod
    def previewing(members=list(), set_=dict()):
        result = dict()
        result['state'] = Common.exchange_state(20000)

        for item in members:
            if not isinstance(item, tuple):
                result['state'] = Common.exchange_state(41204)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，收到 ',
                                                           type(item).__name__, '，源自 ', str(item)])
                return result

            member_type = None
            member_range = None

            if item.__len__() == 3:
                member_type = item[0]
                member_name = item[1]
                member_range = item[2]

            elif item.__len__() == 2:
                member_type = item[0]
                member_name = item[1]

            elif item.__len__() == 1:
                member_name = item[0]

            else:
                result['state'] = Common.exchange_state(41205)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，收到 ',
                                                           str(item.__len__()), '，源自 ', str(item)])
                return result

            if type(member_name).__name__ != 'str':
                result['state'] = Common.exchange_state(41207)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，收到 ',
                                                           type(member_name).__name__, '，源自 ', str(item)])
                return result

            if member_name not in set_:
                result['state'] = Common.exchange_state(41201)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], str(member_name)])
                return result

            if member_type is not None:
                if not isinstance(set_[member_name], member_type):
                    result['state'] = Common.exchange_state(41202)
                    result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，预期类型 ',
                                                               member_type.__name__, '，收到 ',
                                                               type(set_[member_name]).__name__,
                                                               '，源自字段 ', str(member_name)])
                    return result

            if member_range is not None:
                if isinstance(member_range, tuple):
                    if member_range.__len__() < 2:
                        result['state'] = Common.exchange_state(41206)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，预期2个元素，收到 ',
                                                                   str(member_range.__len__()), '，源自 ',
                                                                   str(member_range)])
                        return result

                    if not member_range[0] <= set_[member_name] <= member_range[1]:
                        result['state'] = Common.exchange_state(41203)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，预期取值范围 ',
                                                                   str(member_range), '，收到 ',
                                                                   str(set_[member_name])])
                        return result

                elif isinstance(member_range, list):
                    if member_range.__len__() < 1:
                        result['state'] = Common.exchange_state(41206)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，不可少于1个，收到 ',
                                                                   str(member_range.__len__()), '，源自 ',
                                                                   str(member_range)])
                        return result

                    if set_[member_name] not in member_range:
                        result['state'] = Common.exchange_state(41203)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，预期取值范围 ',
                                                                   str(member_range), '，收到 ',
                                                                   str(set_[member_name])])
                        return result

                else:
                    result['state'] = Common.exchange_state(41206)
                    result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], '，不支持的类型 ',
                                                               type(member_range).__name__])
                    return result

        return result
