import enum
from typing import *

import cooltypes

from frozenchess.abc.enums.Meta import *

__all__ = ["Flag"]


class Flag(
    cooltypes.CoolInt, enum.ReprEnum, enum.Flag, boundary=enum.CONFORM, metaclass=Meta
):
    "This class functions as the base for all enum flags of the project."

    pass
