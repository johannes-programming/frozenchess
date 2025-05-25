import enum
from typing import *

from frozenchess.bases.ables.SubInt import *

__all__ = ["Flag"]


class Flag(SubInt, enum.ReprEnum, enum.Flag, boundary=enum.CONFORM):
    "This class functions as the base for all enum flags of the project."

    pass
