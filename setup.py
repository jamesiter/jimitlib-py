#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'James Iter'
__date__ = '15/4/20'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2015 by James Iter.'

import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


PACKAGE = "jimit"
NAME = "jimit"
DESCRIPTION = "James Iter's common library by python."
AUTHOR = "James Iter"
AUTHOR_EMAIL = "james.iter.cn@gmail.com"
URL = "https://github.com/jamesiter/jimitlib-py.git"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Service Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Linux",
        "Programming Language :: Python",
        "Framework :: None",
        ],
    zip_safe=False,
)