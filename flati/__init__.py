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
from . import flati

VERSION = (0, 1)
__version__ = '0.1'

flatten = flati.flatten
