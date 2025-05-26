from abc import ABC, abstractmethod
from typing import *

__all__ = ["Mirrorable"]


class Mirrorable(ABC):
    @abstractmethod
    def mirror(self) -> Self:
        "This method swaps the players."
        pass
