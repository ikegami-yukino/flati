# -*- coding: utf-8 -*-
def flatten(iterable, ignore=None):
    """Flatten nested iterable object
    Args:
        iterable_obejct (iterable) : required
        ignore (type or tuple) : optional
    Return:
        flattend (generator)

    >>> iterable = [(1, 2, 3), (4, (5, 6))]
    >>> list(flatten(iterable))
    [1, 2, 3, 4, 5, 6]
    >>> iterable = [('abc'), ('def', ('g', 'hi'))]
    >>> list(flatten(iterable, ignore=(str,)))
    ['abc', 'def', 'g', 'hi']
    """
    def _flatten(x, ignore):
        if hasattr(x, '__iter__'):
            if ignore and isinstance(x, ignore):
                yield x
            else:
                for y in x:
                    yield from _flatten(y, ignore)
        else:
            yield x

    yield from _flatten(iterable, ignore)
