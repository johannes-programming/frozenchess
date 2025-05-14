from __future__ import annotations

from enum import IntFlag
from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.FENMod import *

__all__ = ["FlagFENMod"]


class FlagFENMod(FENMod, IntFlag): ...
