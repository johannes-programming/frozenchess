from abc import ABC, abstractmethod
from typing import *


class HasNative(ABC):
    @abstractmethod
    def native(self: Self, /) -> Any:
        "This method returns the native of the instance."
        pass
