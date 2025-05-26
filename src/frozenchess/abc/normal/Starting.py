from abc import ABC, abstractmethod
from typing import *

__all__ = ["Starting"]


class Starting(ABC):
    @classmethod
    @abstractmethod
    def starting(cls: type, /) -> Self:
        "This classmethod returns an instance representing the starting configuration."
        pass
