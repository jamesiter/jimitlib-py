#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

from common import *
import re


class Check(object):

    def __init__(self):
        pass

    @staticmethod
    def previewing(members=None, set_=None):
        """
        :rtype : dict
        :param members: 合法对象的规则描述
        :param set_: 存放对象的集合
        :return: dict格式的检测结果
        """
        if members is None:
            members = []

        if set_ is None:
            set_ = {}

        result = dict()
        result['state'] = Common.exchange_state(20000)

        for item in members:
            if not isinstance(item, tuple):
                result['state'] = Common.exchange_state(41204)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，收到 ',
                                                           type(item).__name__, u'，源自 ', str(item)])
                raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

            member_type = None
            member_range = None
            member_need = True

            if item.__len__() == 4:
                member_type = item[0]
                member_name = item[1]
                member_range = item[2]
                member_need = item[3]

            elif item.__len__() == 3:
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
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，收到 ',
                                                           str(item.__len__()), u'，源自 ', str(item)])
                raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

            if not isinstance(member_name, basestring):
                result['state'] = Common.exchange_state(41207)
                result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，收到 ',
                                                           type(member_name).__name__, u'，源自 ', str(item)])
                raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

            if member_name not in set_:
                if member_need:
                    result['state'] = Common.exchange_state(41201)
                    result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], str(member_name)])
                    raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                else:
                    return result

            if member_type is not None:
                if isinstance(member_type, basestring):
                    if 0 == member_type.find('regex:'):
                        if re.match(member_type[6:], set_[member_name]) is None:
                            result['state'] = Common.exchange_state(41209)
                            raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                elif not isinstance(set_[member_name], member_type):
                    result['state'] = Common.exchange_state(41202)
                    result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，预期类型 ',
                                                               str(member_type), u'，收到 ',
                                                               type(set_[member_name]).__name__,
                                                               u'，源自字段 ', str(member_name)])
                    raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

            if member_range is not None:
                if isinstance(member_range, tuple):
                    if member_range.__len__() < 2:
                        result['state'] = Common.exchange_state(41206)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，预期2个元素，收到 ',
                                                                   str(member_range.__len__()), u'，源自 ',
                                                                   str(member_range)])
                        raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                    if member_type in [basestring, str, unicode, tuple, list, dict]:
                        me = set_[member_name].__len__()
                    else:
                        me = set_[member_name]

                    if not member_range[0] <= me <= member_range[1]:
                        result['state'] = Common.exchange_state(41203)
                        result['state']['sub']['zh-cn'] = ''.join([member_name, result['state']['sub']['zh-cn'],
                                                                   u'，预期取值范围 ', str(member_range), u'，收到 ',
                                                                   str(set_[member_name])])
                        raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                elif isinstance(member_range, list):
                    if member_range.__len__() < 1:
                        result['state'] = Common.exchange_state(41206)
                        result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，不可少于1个，收到 ',
                                                                   str(member_range.__len__()), u'，源自 ',
                                                                   str(member_range)])
                        raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                    if set_[member_name] not in member_range:
                        result['state'] = Common.exchange_state(41203)
                        result['state']['sub']['zh-cn'] = ''.join([member_name, result['state']['sub']['zh-cn'],
                                                                   u'，预期取值范围 ', str(member_range), u'，收到 ',
                                                                   str(set_[member_name])])
                        raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

                else:
                    result['state'] = Common.exchange_state(41206)
                    result['state']['sub']['zh-cn'] = ''.join([result['state']['sub']['zh-cn'], u'，不支持的类型 ',
                                                               type(member_range).__name__])
                    raise ji.PreviewingError(json.dumps(result, ensure_ascii=False))

        return result
