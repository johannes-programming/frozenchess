import abc
import enum

__all__ = ["Meta"]


class Meta(enum.EnumMeta, abc.ABCMeta):
    pass
