import abc
from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["UCIStylable"]


class UCIStylable(abc.ABC):
    @classmethod
    def byUCIStyled(cls, styled: Any) -> Self:
        raise AbstractionError

    def uciStyled(self) -> str:
        raise AbstractionError
