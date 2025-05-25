from typing import *

from frozenchess.utils import *

__all__ = ["Mirrorable"]


class Mirrorable:
    def mirror(self) -> Self:
        "This method swaps the players."
        raise AbstractionError
