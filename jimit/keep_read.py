#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '16/1/17'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import time
import os
import json
import thread
import signal
import threading
import sys


reload(sys)
sys.setdefaultencoding('utf8')


class KeepRead(object):
    """
        配置文件默认路径
            /etc/monitor_log.conf
            通过修改参数 KeepRead.config_path 来替换

        游标持久化默认存储路径
            /var/lib/misc/cursor.ml
            通过修改参数 KeepRead.cursor_path 来替换

        用法:
            设计过滤器方法,输入的参数仅有一个,即每次调用时所读取的行
            @staticmethod
            def filtrator(line=None):
                print line

            首先指定过滤器
            KeepRead.filtrator = filtrator
            启动
            KeepRead.launch()
    """
    # Example:
    # {"/var/log/messages": 2341, "/var/log/nginx/error_log": 3521}
    cursor = {}
    # Example:
    # [
    #   {"path": "/var/log/messages", "start_position": 0},
    #   {"path": "/var/log/nginx/error_log", "start_position": 0}
    # ]
    config = []
    log_file_ino = {}
    log_file_size = {}
    config_path = '/etc/monitor_log.conf'
    cursor_path = '/var/lib/misc/cursor.ml'
    exit_flag = False
    thread_counter = 0
    filtrator = None
    # 默认开启线程锁
    thread_mutex_lock_on = True
    thread_mutex_lock = threading.Lock()

    def __init__(self):
        self.log_path = ''
        self.line = ''

    @classmethod
    def save_cursor(cls):
        dirname = os.path.dirname(cls.cursor_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(cls.cursor_path, 'w') as f:
            f.write(json.dumps(cls.cursor))

    @classmethod
    def restore_cursor(cls):
        if os.path.exists(cls.cursor_path):
            with open(cls.cursor_path) as f:
                cls.cursor = json.load(f)

    @classmethod
    def load_config(cls):
        if os.path.exists(cls.config_path):
            with open(cls.config_path, 'r') as f:
                cls.config = json.load(f)

    @classmethod
    def set_cursor(cls, log_path=None, offset=0):
        cls.cursor[log_path] = offset

    @classmethod
    def get_cursor(cls, log_path=None):
        return cls.cursor[log_path]

    @classmethod
    def increment_thread_counter(cls, number=1):
        cls.thread_counter += number

    @classmethod
    def get_exit_flag(cls):
        return cls.exit_flag

    @classmethod
    # ino for index node number
    def watch_ino(cls):
        cls.increment_thread_counter(1)
        while True:
            if cls.get_exit_flag():
                cls.increment_thread_counter(-1)
                return

            try:
                for item in KeepRead.config:
                    st_stat = os.stat(item['path'])
                    st_ino = st_stat.st_ino
                    st_size = st_stat.st_size
                    if item['path'] not in cls.log_file_ino:
                        cls.log_file_ino[item['path']] = dict()
                        cls.log_file_ino[item['path']]['changed'] = False
                        cls.log_file_ino[item['path']]['last'] = st_ino

                    if cls.log_file_ino[item['path']]['last'] != st_ino:
                        cls.log_file_ino[item['path']]['changed'] = True
                        cls.log_file_ino[item['path']]['last'] = st_ino

                    if item['path'] not in cls.log_file_size:
                        cls.log_file_size[item['path']] = dict()
                        cls.log_file_size[item['path']]['changed'] = False
                        cls.log_file_size[item['path']]['last'] = st_size

                    # 只有监控的文件缩小时, 才记录改变状态
                    if cls.log_file_size[item['path']]['last'] > st_size:
                        cls.log_file_size[item['path']]['changed'] = True

                    # 记录当前文件大小, 如果监控的文件基础大小太小, 而且又在一个周期(这里是1秒)内瞬间从0增至或超过当前大小, 那么在这里是觉察不到的.
                    cls.log_file_size[item['path']]['last'] = st_size

            except OSError:
                pass
            except:
                cls.increment_thread_counter(-1)
                raise

            time.sleep(1)

    @classmethod
    def get_ino_changed(cls, path=None):
        if path not in cls.log_file_ino:
            return False
        return cls.log_file_ino[path]['changed']

    @classmethod
    def reset_ino_changed(cls, path=None):
        cls.log_file_ino[path]['changed'] = False

    @classmethod
    def get_size_changed(cls, path=None):
        if path not in cls.log_file_size:
            return False
        return cls.log_file_size[path]['changed']

    @classmethod
    def reset_size_changed(cls, path=None):
        cls.log_file_size[path]['changed'] = False

    def monitor(self, replace=False):
        # 线程替换时不做增量统计
        if not replace:
            self.increment_thread_counter(1)
        # 如果被监控的文件不存在时,则一直循环尝试打开
        while True:
            try:
                with open(self.log_path, 'rU') as f:
                    offset = self.get_cursor(log_path=self.log_path)
                    if offset > 0:
                        f.seek(offset)
                    while True:
                        if self.get_exit_flag():
                            self.increment_thread_counter(-1)
                            return

                        self.line = f.readline()
                        if self.get_cursor(log_path=self.log_path) == f.tell():
                            if self.get_ino_changed(self.log_path):
                                self.reset_ino_changed(self.log_path)
                                kr = KeepRead()
                                kr.log_path = self.log_path
                                KeepRead.cursor[kr.log_path] = 0
                                return thread.start_new_thread(kr.monitor, (True, ))

                            if self.get_size_changed(self.log_path):
                                self.reset_size_changed(self.log_path)
                                f.seek(0)

                            time.sleep(1)
                            continue

                        self.set_cursor(log_path=self.log_path, offset=f.tell())
                        self.dispose()

            except IOError:
                time.sleep(1)
            except:
                self.increment_thread_counter(-1)
                raise

    def dispose(self):
        if self.thread_mutex_lock_on:
            self.thread_mutex_lock.acquire()

        KeepRead.filtrator(self.line)

        if self.thread_mutex_lock_on:
            self.thread_mutex_lock.release()

    @classmethod
    def signal_handle(cls, signum=0, frame=None):
        cls.exit_flag = True

    @staticmethod
    def launch():
        # ml for monitor log
        signal.signal(signal.SIGTERM, KeepRead.signal_handle)
        signal.signal(signal.SIGINT, KeepRead.signal_handle)
        KeepRead.load_config()
        KeepRead.restore_cursor()
        thread.start_new_thread(KeepRead.watch_ino, ())
        for item in KeepRead.config:
            kr = KeepRead()
            kr.log_path = item['path']

            if 'start_position' in item:
                KeepRead.cursor[kr.log_path] = item['start_position']
            elif kr.log_path not in KeepRead.cursor:
                KeepRead.cursor[kr.log_path] = 0

            thread.start_new_thread(kr.monitor, ())

        # 避免上面的for语句过快,导致线程还没有执行increment_thread_counter,
        # 就进入下面的while语句,这样thread_counter此时还为0,故而会跳过线程等待逻辑
        time.sleep(1)
        # 变通的方式实现线程等待目的
        while KeepRead.thread_counter > 0:
            time.sleep(1)
        KeepRead.save_cursor()
        print 'Bye-bye!'

