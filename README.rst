flati
==========

|pyversion| |version| |license| |download| |nowarnonukes|

Flatten nested iterable object (Pure-Python implementation)

Japanese document is available: https://qiita.com/yukinoi/items/9570c76034c28bdae0a8

Installation
==============

::

 $ pip install flati


Usage
============

.. code:: python

  import flati

  iterable = [(1, 2, 3), (4, (5, 6))]
  list(flati.flatten(iterable))
  # => [1, 2, 3, 4, 5, 6]

  # The flati.flatten function returns a generator
  import types
  isinstance(flati.flatten(iterable), types.GeneratorType)
  # => True

  # If you want to avoid flattening specific type, then use "ignore" parameter
  iterable = [('abc'), ('def', ('g', 'hi'))]
  list(flati.flatten(iterable, ignore=str))
  # => ['abc', 'def', 'g', 'hi']

  # The flatten_non_str function is alias of "flatten(iterable, ignore=str)"
  iterable = [('abc'), ('def', ('g', 'hi'))]
  list(flati.flatten_non_str(iterable))
  # => ['abc', 'def', 'g', 'hi']

Tips
------
If you want to flatten numpy.ndarray, I recommend using following methods:

* numpy.ravel()
* ndarray.reshape(-1)
* ndarray.flatten()  # This method is a bit slow because it makes a copy

Contribution
=============
Contributions are welcome.

See https://github.com/ikegami-yukino/flati/blob/master/CONTRIBUTING.md


.. |pyversion| image:: https://img.shields.io/pypi/pyversions/flati.svg
    :target: http://pypi.python.org/pypi/flati/
    :alt: Python version

.. |version| image:: https://img.shields.io/pypi/v/flati.svg
    :target: http://pypi.python.org/pypi/flati/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/flati.svg
    :target: http://pypi.python.org/pypi/flati/
    :alt: license

.. |download| image:: https://static.pepy.tech/personalized-badge/flati?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads
    :target: https://pepy.tech/project/flati
    :alt: download

.. |nowarnonukes| image:: https://img.shields.io/badge/NO%20WAR-NO%20NUKES-brightgreen
    :alt: NO WAR
