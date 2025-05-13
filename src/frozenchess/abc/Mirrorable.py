import abc
from typing import *

__all__ = ["Mirrorable"]


class Mirrorable(abc.ABC):
    @abc.abstractmethod
    def mirror(self) -> Self: ...
