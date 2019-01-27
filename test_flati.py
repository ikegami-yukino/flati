# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import flati


def test_flatten():
    iterable = [(1, 2, 3), (4, (5, 6))]
    expected = [1, 2, 3, 4, 5, 6]
    assert_equal(list(flati.flatten(iterable)), expected)

    iterable = [('abc'), ('def', ('g', 'hi'))]
    expected = ['abc', 'def', 'g', 'hi']
    assert_equal(list(flati.flatten(iterable, ignore=str)), expected)
