import operator
from typing import *

__all__ = ["IntMod"]


class IntMod(int):
    # private helper methods
    def __op1(self: Self, /, op: Callable) -> Self:
        cls: type = type(self)
        x: int = int(self)
        z: int = op(x)
        ans: Self = cls(z)
        return ans

    def __op2(cls: type, /, op: Callable, a: SupportsInt, b: SupportsInt) -> Self:
        x: int = int(a)
        y: int = int(b)
        z: int = op(x, y)
        ans: Self = cls(z)
        return ans

    # new
    def __new__(cls: type, value: SupportsInt) -> Self:
        v: int = int(value) % cls._mod()
        ans: Self = int.__new__(cls, v)
        return ans

    # binary operations
    def __add__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.add, self, other)

    def __and__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.and_, self, other)

    def __floordiv__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.floordiv, self, other)

    def __lshift__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.lshift, self, other)

    def __mod__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.mod, self, other)

    def __mul__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.mul, self, other)

    def __or__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.or_, self, other)

    def __pow__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.pow, self, other)

    def __rshift__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.rshift, self, other)

    def __sub__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.sub, self, other)

    def __xor__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.or_, self, other)

    # reflected operations
    def __radd__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.add, other, self)

    def __rand__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.and_, other, self)

    def __rfloordiv__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.floordiv, other, self)

    def __rlshift__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.lshift, other, self)

    def __rmod__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.mod, other, self)

    def __rmul__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.mul, other, self)

    def __rpow__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.pow, other, self)

    def __ror__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.or_, other, self)

    def __rrshift__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.rshift, other, self)

    def __rsub__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.sub, other, self)

    def __rxor__(self: Self, other: SupportsInt) -> Self:
        return self.__op2(operator.xor_, other, self)

    # Unary operations
    def __invert__(self: Self, /):
        return self.__op1(operator.invert, self)

    def __neg__(self: Self, /):
        return self.__op1(operator.neg, self)

    def __pos__(self: Self, /):
        return self.__op1(operator.pos, self)
