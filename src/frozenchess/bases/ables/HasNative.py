from typing import *

from frozenchess.utils import *


class HasNative:
    def native(self: Self, /) -> Any:
        "This method returns the native of the instance."
        raise AbstractionError
