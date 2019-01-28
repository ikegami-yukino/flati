# -*- coding: utf-8 -*-
flatten = lambda x, ignore=None: (z for y in x for z in \
        (flatten(y) if hasattr(y, '__iter__') and not (ignore and isinstance(y, ignore)) else (y,)))
