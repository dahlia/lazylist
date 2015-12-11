``lazylist``
============

.. image:: https://badge.fury.io/py/lazylist.svg
   :alt: PyPI
   :target: https://pypi.python.org/pypi/lazylist

.. image:: https://travis-ci.org/dahlia/lazylist.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/dahlia/lazylist

This small package provides a proxy list to a list-returning function:

>>> from lazylist import LazyList
>>> l = LazyList(lambda: x)
>>> x = [1, 2, 3]
>>> list(l)
[1, 2, 3]

More precisely, view function doesn't have to return an exact ``list``,
but an any squence object e.g. ``str``, ``tuple``:

>>> x = "hello"
>>> list(l)
['h', 'e', 'l', 'l', 'o']

It satisfies ``collections.abc.Sequence`` protocol:

>>> from collections import Sequence
>>> isinstance(l, Sequence)
True
>>> l[-1]
'o'
>>> len(l)
5

However, it doesn't satisfy ``collections.abc.MutableSequence`` protocol.
In other words, it's immutable:

>>> from collections import MutableSequence
>>> isinstance(l, MutableSequence)
False
>>> l[0] = 'H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'LazyList' object does not support item assignment

Distributed under LGPLv3 or higher.
