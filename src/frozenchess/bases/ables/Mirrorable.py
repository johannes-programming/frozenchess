from typing import *

from frozenchess.utils import *

__all__ = ["Mirrorable"]


class Mirrorable:
    def mirror(self) -> Self:
        raise AbstractionError
