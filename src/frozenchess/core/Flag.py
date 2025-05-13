from __future__ import annotations

import enum
import operator
from typing import *

__all__ = ["Flag"]


class Flag(enum.IntEnum):
    @classmethod
    def __op1(cls, a: SupportsIndex, /, op: Callable) -> Self:
        x: int = operator.index(a)
        z: int = op(x)
        z %= len(cls)
        return cls(z)

    @classmethod
    def __op2(cls, a: SupportsIndex, b: SupportsIndex, /, op: Callable) -> Self:
        x: int = operator.index(a)
        y: int = operator.index(b)
        z: int = op(x, y)
        z %= len(cls)
        return cls(z)

    #
    def __invert__(self) -> Self:
        return self.__op1(self, operator.invert)

    # Binary operators
    def __and__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.and_)

    def __or__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.or_)

    def __xor__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.xor)

    def __add__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.add)

    def __sub__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.sub)

    def __mul__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.mul)

    def __floordiv__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.floordiv)

    def __mod__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.mod)

    def __pow__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.pow)

    def __lshift__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.lshift)

    def __rshift__(self, other: SupportsIndex, /) -> Self:
        self.__op2(self, other, operator.rshift)

    # Reverse operators
    def __rand__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.and_)

    def __ror__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.or_)

    def __rxor__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.xor)

    def __radd__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.add)

    def __rsub__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.sub)

    def __rmul__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.mul)

    def __rfloordiv__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.floordiv)

    def __rmod__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.mod)

    def __rpow__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.pow)

    def __rlshift__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.lshift)

    def __rrshift__(self, other: SupportsIndex, /) -> Self:
        self.__op2(other, self, operator.rshift)
