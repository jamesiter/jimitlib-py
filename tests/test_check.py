#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/25'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
sys.path.append("..")
from jimit.check import Check
import jimit as ji
import json
import unittest


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
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41201', ret['state']['sub']['code'])

        form_rules = [
            (str, 'k')
        ]
        form = {
            'k': 123
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41202', ret['state']['sub']['code'])

        form_rules = [
            (str, 'k', ['F', 'M'])
        ]
        form = {
            'k': 'v'
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41203', ret['state']['sub']['code'])

        form_rules = [
            "str, 'k', ['F', 'M']"
        ]
        form = {
            'k': 'v'
        }
        try:
            Check.previewing(form_rules, form)
        except Exception as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41204', ret['state']['sub']['code'])

        form_rules = [
            (str, )
        ]
        form = {
            'k': 'v'
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41207', ret['state']['sub']['code'])

        form_rules = [
            ('regex:^[a-z0-9]+([._][a-z0-9]+)*@[a-z0-9]+([-][a-z0-9]+)*\.[a-z]+$', 'email')
        ]
        form = {
            'email': 'james.iter.cn@gmail.com'
        }
        try:
            ret = Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('200', ret['state']['code'])

        form_rules = [
            ('regex:^[a-z0-9]+([._][a-z0-9]+)*@[a-z0-9]+([-][a-z0-9]+)*\.[a-z]+$', 'email')
        ]
        form = {
            'email': '.james.iter.cn@gmail.com'
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41209', ret['state']['sub']['code'])

        form_rules = [
            (str, 'email', (8, 64))
        ]
        form = {
            'email': 'a@b.c'
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('41203', ret['state']['sub']['code'])

        form_rules = [
            (str, 'email', (8, 64), False)
        ]
        form = {
            'xmail': 'a@b.c'
        }
        try:
            ret = Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('200', ret['state']['code'])

        form_rules = [
            (int, 'number', (0, 100))
        ]
        form = {
            'number': 10
        }
        try:
            Check.previewing(form_rules, form)
        except ji.PreviewingError as e:
            ret = json.loads(e.__str__())
        self.assertEqual('200', ret['state']['code'])


if __name__ == '__main__':
    unittest.main()
