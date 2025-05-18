from typing import *

from frozenchess.bases.abstraction import *

__all__ = ["Mirrorable"]


class Mirrorable:
    def mirror(self) -> Self:
        raise AbstractionError
