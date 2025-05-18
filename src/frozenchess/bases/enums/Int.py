import enum
import operator
from typing import *

__all__ = ["SubInt"]


class Operational:
    def __op1(self: Self, /, operation: Callable) -> Self:
        return (type(self))(operation(operator.index(self)))

    @classmethod
    def __op2(
        cls: type, /, operation: Callable, left: SupportsIndex, right: SupportsIndex
    ) -> Self:
        return cls(operation(operator.index(left), operator.index(right)))

    # unary
    def __neg__(self: Self, /) -> Self:
        return self.__op1(operator.neg)

    def __pos__(self: Self, /) -> Self:
        return self.__op1(operator.pos)

    def __invert__(self: Self, /) -> Self:
        return self.__op1(operator.invert)

    def __abs__(self: Self, /) -> Self:
        return self.__op1(operator.abs)

    # normal binary
    def __add__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.add, self, other)

    def __sub__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.sub, self, other)

    def __mul__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.mul, self, other)

    def __floordiv__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.floordiv, self, other)

    def __mod__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.mod, self, other)

    def __pow__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.pow, self, other)

    def __lshift__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.lshift, self, other)

    def __rshift__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.rshift, self, other)

    def __and__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.and_, self, other)

    def __or__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.or_, self, other)

    def __xor__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.xor, self, other)

    # reverse binary
    def __radd__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.add, self, other)

    def __rsub__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.sub, self, other)

    def __rmul__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.mul, self, other)

    def __rfloordiv__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.floordiv, self, other)

    def __rmod__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.mod, self, other)

    def __rpow__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.pow, self, other)

    def __rlshift__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.lshift, self, other)

    def __rrshift__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.rshift, self, other)

    def __rand__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.and_, self, other)

    def __ror__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.or_, self, other)

    def __rxor__(self: Self, other: SupportsIndex, /) -> Self:
        return self.__op2(operator.xor, self, other)
