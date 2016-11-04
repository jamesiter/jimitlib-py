#!/usr/bin/env python
# -*- coding: utf-8 -*-


from jimit import Common


__author__ = 'James Iter'
__date__ = '15/5/16'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'


router_table = {}


class Router(object):

    def __init__(self):
        pass

    @staticmethod
    def not_found(content):
        return Common.exchange_state(50100)

    @staticmethod
    def launcher(**kwargs):
        action = kwargs.get('action', None)
        content = kwargs.get('content', None)
        return router_table.get(action, Router.not_found)(content)
