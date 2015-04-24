#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/25'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import sys
import json
import jimit as ji

reload(sys)
sys.setdefaultencoding('utf8')

needs = [(int, 'age', (10, 100)),
         (int, 'name'),
         (str, 'sex', ['F', 'M'])]

content = {
    'age': 10,
    'name': 'iter',
    'sex': 'F'
}

print json.dumps(ji.Check.previewing(needs, content), ensure_ascii=False)