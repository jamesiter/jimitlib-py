#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/25'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.check import Check
import unittest

reload(sys)
sys.setdefaultencoding('utf8')


class TestCheck(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_previewing(self):

        form_rules = [
            (int, 'k', (10, 100))
        ]
        form = {
            'k': 10
        }
        self.assertEqual('200', Check.previewing(form_rules, form)['state']['code'])

        form_rules = [
            (int, 'k', (10, 100))
        ]
        form = {
        }
        self.assertEqual('41201', Check.previewing(form_rules, form)['state']['sub']['code'])

        form_rules = [
            (str, 'k')
        ]
        form = {
            'k': 123
        }
        self.assertEqual('41202', Check.previewing(form_rules, form)['state']['sub']['code'])

        form_rules = [
            (str, 'k', ['F', 'M'])
        ]
        form = {
            'k': 'v'
        }
        self.assertEqual('41203', Check.previewing(form_rules, form)['state']['sub']['code'])

        form_rules = [
            "str, 'k', ['F', 'M']"
        ]
        form = {
            'k': 'v'
        }
        self.assertEqual('41204', Check.previewing(form_rules, form)['state']['sub']['code'])

        form_rules = [
            (str, )
        ]
        form = {
            'k': 'v'
        }
        self.assertEqual('41207', Check.previewing(form_rules, form)['state']['sub']['code'])


if __name__ == '__main__':
    unittest.main()