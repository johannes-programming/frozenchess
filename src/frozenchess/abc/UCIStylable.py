import abc
from typing import *

__all__ = ["UCIStylable"]


class UCIStylable(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def byUCIStyled(cls, styled: Any) -> Self: ...
    @abc.abstractmethod
    def uciStyled(self) -> str: ...
