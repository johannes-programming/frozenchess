import enum
from typing import *

__all__ = ["Flag"]


class Flag(int, enum.ReprEnum, enum.Flag, boundary=enum.CONFORM):
    pass
