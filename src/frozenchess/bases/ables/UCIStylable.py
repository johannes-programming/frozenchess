from typing import *

from frozenchess.utils import *

__all__ = ["UCIStylable"]


class UCIStylable:
    @classmethod
    def byUCIStyled(cls: type, /, styled: Any) -> Self:
        "This classmethod returns an instance created from UCI styled input."
        raise AbstractionError

    def uciStyled(self: Self, /) -> str:
        raise AbstractionError
