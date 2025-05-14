from enum import EnumMeta
from typing import *

__all__ = ["ModMeta"]


class ModMeta(EnumMeta):
    def __call__(cls: type, value: Any, *args: Any, **kwargs: Any) -> Self:
        value = value % cls._mod()
        return super().__call__(value, *args, **kwargs)
