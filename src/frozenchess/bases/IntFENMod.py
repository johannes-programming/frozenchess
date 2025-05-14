from __future__ import annotations

from enum import IntEnum
from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.FENMod import *

__all__ = ["IntFENMod"]


class IntFENMod(FENMod, IntEnum): ...
