from __future__ import annotations

from typing import *

from frozenchess.bases.AbstractionError import *
from frozenchess.bases.ModMeta import *

__all__ = ["Mod"]


class Mod(metaclass=ModMeta):
    @classmethod
    def _mod(cls: type) -> int:
        raise AbstractionError
