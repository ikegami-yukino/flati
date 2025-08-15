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
    >>> list(flati.flatten_non_str(iterable))  # Alias of `flatten(iterable, ignore=str)`
    ['abc', 'def', 'g', 'hi']
"""
from sys import version_info
if version_info < (3,):
    from . import py2
    flatten = py2.flatten
else:
    from . import py3
    flatten = py3.flatten

VERSION = (0, 2, 0)
__version__ = '0.2.0'

def flatten_non_str(iterable, ignore=None):
    """Flatten nested iterable object, ignoring strings.
    This function is a convenience wrapper around `flatten` that ignores `str` type by default.

    Args:
        iterable: An iterable to flatten.
        ignore: A type or tuple of types to not flatten.

    Yields:
        The items from the flattened iterable, but str are unchanged.

    >>> iterable = [('abc'), ('def', ('g', 'hi'))]
    >>> list(flatten_non_str(iterable))
    ['abc', 'def', 'g', 'hi']
    >>> iterable = ['abc', ['def', ('g', 'hi')]]
    >>> list(flatten_non_str(iterable, ignore=tuple))
    ['abc', 'def', ('g', 'hi')]
    """
    if ignore is None:
        ignore = str
    else:
        if isinstance(ignore, str):
            ignore = str
        # Convert ignore to a tuple of types, always including str
        elif isinstance(ignore, type):
            ignore = (ignore, str)
        elif isinstance(ignore, (list, tuple, set, frozenset)):
            # Filter only type objects and add str
            ignore_types = tuple(t for t in ignore if isinstance(t, type))
            ignore = ignore_types + (str,)
    yield from flatten(iterable, ignore=ignore)

__license__ = 'MIT License'
