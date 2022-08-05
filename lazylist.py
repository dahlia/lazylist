import collections

try:
    from collections import Sequence
except ImportError:
    # >=Python 3.10
    from collections.abc import Sequence

__all__ = 'LazyList',
__version__ = '0.9.1'


class LazyList(Sequence):
    """An immutable proxy sequence to a given ``view_function``."""

    def __init__(self, view_function):
        if not callable(view_function):
            raise TypeError('expected callable')
        self.view_function = view_function

    @property
    def raw_value(self):
        result = self.view_function()
        if not isinstance(result, Sequence):
            raise TypeError(repr(result) + ' is not a sequence')
        return result

    def __iter__(self):
        return iter(self.raw_value)

    def __len__(self):
        return len(self.raw_value)

    def __getitem__(self, index):
        return self.raw_value[index]

    def __contains__(self, element):
        return element in self.raw_value
