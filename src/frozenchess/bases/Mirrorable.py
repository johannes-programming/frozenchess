import abc
from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["Mirrorable"]


class Mirrorable(abc.ABC):
    def mirror(self) -> Self:
        raise AbstractionError
