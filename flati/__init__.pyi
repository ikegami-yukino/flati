from typing import Any, Generator, Iterable, Type, Optional, Union

from . import py3

__all__ = ['flatten', 'flatten_non_str']
flatten = py3.flatten

_IgnoreType = Union[str, Type[Any] | tuple[Type[Any], ...]]


def flatten_non_str(
    iterable: Iterable[Any],
    ignore: Optional[_IgnoreType] = None,
) -> Generator[Any, None, None]: ...
