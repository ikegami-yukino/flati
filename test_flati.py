# -*- coding: utf-8 -*-
import flati


def test_flatten():
    iterable = [(1, 2, 3), (4, (5, 6))]
    expected = [1, 2, 3, 4, 5, 6]
    assert list(flati.flatten(iterable)) == expected

    iterable = [('abc'), ('def', ('g', 'hi'))]
    expected = ['abc', 'def', 'g', 'hi']
    assert list(flati.flatten(iterable, ignore=str)) == expected


def test_flatten_non_str():
    iterable = [('abc'), ('def', ('g', 'hi'))]
    expected = ['abc', 'def', 'g', 'hi']
    assert list(flati.flatten_non_str(iterable)) == expected

    iterable = ['abc', ['def', ('g', 'hi')]]
    expected = ['abc', 'def', ('g', 'hi')]
    assert list(flati.flatten_non_str(iterable, ignore=tuple)) == expected

    iterable = ['abc', ['def', set(('g', 'hi')), ('j', 'kl')]]
    expected = ['abc', 'def', set(('g', 'hi')), ('j', 'kl')]
    assert list(flati.flatten_non_str(iterable, ignore=(set, tuple))) == expected
