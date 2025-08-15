from typing import Any, Generator, Iterable, Type, Union, Optional

_IgnoreType = Union[str, Type[Any] | tuple[Type[Any], ...]]


def flatten(
    iterable: Iterable[Any],
    ignore: Optional[_IgnoreType] = None,
) -> Generator[Any, None, None]: ...
