# -*- coding: utf-8 -*-
"""Flati - Flatten nested iterable object

Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    >>> import flati
    >>> iterable = [(1, 2, 3), (4, (5, 6))]
    >>> list(flati.flatten(iterable))
    [1, 2, 3, 4, 5, 6]
    >>> iterable = [('abc'), ('def', ('g', 'hi'))]
    >>> list(flati.flatten(iterable, ignore=(str,)))
    ['abc', 'def', 'g', 'hi']
"""
from sys import version_info
if version_info < (3,):
    from . import py2
    flatten = py2.flatten
else:
    from . import py3
    flatten = py3.flatten

VERSION = (0, 1, 2)
__version__ = '0.1.2'
