import abc
from typing import *

__all__ = ["FENStylable"]


class FENStylable(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def byFENStyled(cls, styled: Any) -> Self: ...
    @abc.abstractmethod
    def fenStyled(self) -> str: ...
