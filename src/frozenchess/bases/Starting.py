import abc
from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["Starting"]


class Starting(abc.ABC):
    @classmethod
    def starting(cls) -> Self:
        raise AbstractionError
