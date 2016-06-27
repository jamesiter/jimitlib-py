#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
参考链接: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
终端测试命令: printf '\e[1;33;40mABC\e[0m'
"""


from enum import Enum


__author__ = 'James Iter'
__date__ = '16/6/27'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2016 by James Iter.'


class ForeGround(Enum):
    # 黑
    BLACK = '30'
    # 红
    RED = '31'
    # 绿
    GREEN = '32'
    # 黄
    YELLOW = '33'
    # 蓝
    BLUE = '34'
    # 紫红
    MAGENTA = '35'
    # 青
    CYAN = '36'
    # 白
    WHITE = '37'


class BackGround(Enum):
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'


class Effect(Enum):
    # 常规
    NORMAL = '0'
    # 粗体
    BOLD = '1'
    # 微弱
    FAINT = '2'
    # 下划线
    UNDER_LINE = '4'
    # 慢闪烁
    BLINK_SLOW = '5'
    # 快闪烁
    BLINK_RAPID = '6'
    # 字体\背景色替换
    REVERSE = '7'
    # 隐藏
    CONCEAL = '8'


class Color(object):
    def __init__(self, **kwargs):
        self.effect = kwargs.get('effect', Effect.NORMAL)
        self.fore_ground = kwargs.get('fore_ground', ForeGround.WHITE)
        self.back_ground = kwargs.get('back_ground', BackGround.BLACK)
        self.content = kwargs.get('content', '')

    def get(self):
        return ''.join(['\033[', self.effect, ';', self.fore_ground, ';', self.back_ground, 'm', self.content,
                        '\033[0m'])

    @staticmethod
    def error(content=''):
        color = Color(effect=Effect.BOLD.value, fore_ground=ForeGround.RED.value, back_ground=BackGround.BLACK.value,
                      content=content)
        return color.get()

    @staticmethod
    def error_blink(content=''):
        color = Color(effect=';'.join([Effect.BOLD.value, Effect.BLINK_SLOW.value]), fore_ground=ForeGround.RED.value,
                      back_ground=BackGround.BLACK.value, content=content)
        return color.get()

    @staticmethod
    def warning(content=''):
        color = Color(effect=Effect.BOLD.value, fore_ground=ForeGround.YELLOW.value, back_ground=BackGround.BLACK.value,
                      content=content)
        return color.get()

    @staticmethod
    def warning_blink(content=''):
        color = Color(effect=';'.join([Effect.BOLD.value, Effect.BLINK_SLOW.value]), fore_ground=ForeGround.YELLOW.value,
                      back_ground=BackGround.BLACK.value, content=content)
        return color.get()

    @staticmethod
    def succeed(content=''):
        color = Color(effect=Effect.BOLD.value, fore_ground=ForeGround.GREEN.value, back_ground=BackGround.BLACK.value,
                      content=content)
        return color.get()

    @staticmethod
    def succeed_blink(content=''):
        color = Color(effect=';'.join([Effect.BOLD.value, Effect.BLINK_SLOW.value]), fore_ground=ForeGround.GREEN.value,
                      back_ground=BackGround.BLACK.value, content=content)
        return color.get()
