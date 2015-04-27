#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import copy
from state_code import *


class Commons():

    def __init__(self):
        pass

    @staticmethod
    def exchange_state(code):
        if not isinstance(code, int):
            result = Commons.exchange_state(50001)
            return result

        trunk_code = int(code / 100)
        if str(trunk_code) not in index_state['trunk']:
            result = Commons.exchange_state(50002)
            return result

        result = copy.copy(index_state['trunk'][(str(trunk_code))])

        if str(code) in index_state['branch']:
            result['sub'] = copy.copy(index_state["branch"][(str(code))])

        return result
