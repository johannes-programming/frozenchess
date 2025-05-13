import abc
from typing import *

__all__ = ["Starting"]


class Starting(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def starting(cls) -> Self: ...
