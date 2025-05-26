import abc
from typing import *

__all__ = ["FENStylable"]


class FENStylable(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def byFENStyled(cls: type, /, styled: Any) -> Self:
        "This classmethod returns an instance created from FEN styled input."
        pass

    @abc.abstractmethod
    def fenStyled(self: Self, /) -> str:
        "This method returns a string in FEN style."
        pass
