from abc import ABCMeta
from enum import EnumMeta

__all__ = ["ABCEnumMeta"]


class ABCEnumMeta(ABCMeta, EnumMeta): ...
