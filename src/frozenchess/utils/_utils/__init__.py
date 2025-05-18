import inspect
from typing import *

import keyalias
import normedtuple
from datarepr import datarepr

__all__ = ["antidict", "tuplize"]


def antidict(dictionary: dict) -> dict:
    ans: dict = dict()
    k: Any = None
    v: Any = None
    for k, v in dictionary.items():
        ans[v] = k
    return ans


def tuplize(norm: Callable) -> type:
    ans: type = normedtuple.normedtuple(norm)
    names: list = tuplize_keywords(ans)
    tuplize_alias(ans, names)
    ans.__repr__ = tuplize_repr(names)
    return ans


def tuplize_alias(cls: type, names: list):
    kwargs: dict = dict()
    i: int = 0
    n: str = ""
    for i, n in enumerate(names):
        kwargs[n] = i
    keyalias.classdecorator(cls, **kwargs)


def tuplize_repr(names: list) -> Callable:
    def __repr__(self: Self, /) -> str:
        "This magic method implements repr(self)."
        t: str = type(self).__name__
        i: int = 0
        n: str = ""
        d: dict = dict()
        for i, n in enumerate(names):
            d[n] = self[i]
        ans: str = datarepr(t, **d)
        return ans

    return __repr__


def tuplize_keywords(cls: type):
    sig: inspect.Signature = inspect.signature(cls)
    ans: list = list()
    for name, param in sig.parameters.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            ans.append(name)
    return ans
