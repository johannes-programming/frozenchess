from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["Mirrorable"]


class Mirrorable:
    def mirror(self) -> Self:
        raise AbstractionError
