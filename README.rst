flati
==========
|travis| |coveralls| |pyversion| |version| |license|

Flatten nested iterable object


INSTALLATION
==============

::

 $ pip install flati


USAGE
============

.. code:: python

  import flati

  iterable = [(1, 2, 3), (4, (5, 6))]
  list(flati.flatten(iterable))
  # => [1, 2, 3, 4, 5, 6]

  # flati.flatten() returns a generator
  import types
  isinstance(flati.flatten(iterable), types.GeneratorType)
  # => True

  iterable = [('abc'), ('def', ('g', 'hi'))]
  list(flati.flatten(iterable, ignore=str))
  # => ['abc', 'def', 'g', 'hi']



.. |travis| image:: https://travis-ci.org/ikegami-yukino/flati.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/flati
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/flati/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/flati?branch=master
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/flati.svg

.. |version| image:: https://img.shields.io/pypi/v/flati.svg
    :target: http://pypi.python.org/pypi/flati/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/flati.svg
    :target: http://pypi.python.org/pypi/flati/
    :alt: license
