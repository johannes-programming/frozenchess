from typing import *

__all__ = ["antidict"]


def antidict(dictionary: dict) -> dict:
    ans: dict = dict()
    k: Any = None
    v: Any = None
    for k, v in dictionary.items():
        ans[v] = k
    return ans
