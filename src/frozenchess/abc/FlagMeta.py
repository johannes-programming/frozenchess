from typing import *

from frozenchess.abc.ABCEnumMeta import ABCEnumMeta

__all__ = ["FlagMeta"]


class FlagMeta(ABCEnumMeta):
    def __call__(cls: type, value: Any, *args: Any, **kwargs: Any) -> Self:
        value = value % cls._mod()
        return super().__call__(value, *args, **kwargs)
