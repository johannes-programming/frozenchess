from abc import ABCMeta
from enum import EnumMeta

__all__ = ["FlagMeta"]


class FlagMeta(EnumMeta, ABCMeta):
    def __call__(cls, value, *args, **kwargs):
        value = value % cls._MOD
        return super().__call__(value, *args, **kwargs)
