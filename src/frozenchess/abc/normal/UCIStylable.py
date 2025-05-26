from abc import ABC, abstractmethod
from typing import *

__all__ = ["UCIStylable"]


class UCIStylable(ABC):
    @classmethod
    @abstractmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        "This classmethod returns an instance created from UCI styled input."
        pass

    @abstractmethod
    def uciStyled(self: Self, /) -> str:
        pass
