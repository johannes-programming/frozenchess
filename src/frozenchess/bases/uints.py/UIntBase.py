import operator
from typing import *

from frozenchess.bases.AbstractionError import *

__all__ = ["UIntBase"]


class UIntBase(int):
    @classmethod
    def modulus(cls: type, /) -> int:
        raise AbstractionError

    # op
    def __op1(self: Self, /, op: Callable) -> Self:
        "This private method implements unary operations."
        return type(self)(op(self))

    @classmethod
    def __op2(
        cls: type,
        /,
        op: Callable,
        a: SupportsInt,
        b: SupportsInt,
    ) -> Self:
        "This classmethod implements binary operations."
        x: int = int(a)
        y: int = int(b)
        z: int = op(x, y)
        ans: Self = cls(z)
        return ans

    # new
    def __new__(cls: type, /, *args: Any, **kwargs: Any) -> Self:
        "This magic returns a new instance."
        i: int = int(*args, **kwargs) % cls.modulus()
        ans: Self = int.__new__(cls, i)
        return ans

    # unary
    def __invert__(self: Self, /) -> Self:
        "This magic method implements ~self."
        return self.__op1(operator.invert, self)

    def __neg__(self: Self, /) -> Self:
        "This magic method implements -self."
        return self.__op1(operator.neg, self)

    def __pos__(self: Self, /) -> Self:
        "This magic method implements +self."
        return self.__op1(operator.pos, self)

    # binary
    def __add__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self+other."
        return self.__op2(operator.add, self, other)

    def __and__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self&other."
        return self.__op2(operator.and_, self, other)

    def __divmod__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements divmod(self, other)."
        return self // other, self % other

    def __floordiv__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self//other."
        return self.__op2(operator.floordiv, self, other)

    def __lshift__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self<<other."
        return self.__op2(operator.lshift, self, other)

    def __mod__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self%other."
        return self.__op2(operator.mod, self, other)

    def __mul__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self*other."
        return self.__op2(operator.mul, self, other)

    def __or__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self|other."
        return self.__op2(operator.or_, self, other)

    def __pow__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self**other."
        return self.__op2(operator.pow, self, other)

    def __rshift__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self>>other."
        return self.__op2(operator.rshift, self, other)

    def __sub__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self-other."
        return self.__op2(operator.sub, self, other)

    def __xor__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements self^other."
        return self.__op2(operator.xor, self, other)

    # reverse
    def __radd__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other+self."
        return self.__op2(operator.add, other, self)

    def __rand__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other&self."
        return self.__op2(operator.and_, other, self)

    def __rdivmod__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements divmod(other, self)."
        return other // self, other % self

    def __rfloordiv__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other//self."
        return self.__op2(operator.floordiv, other, self)

    def __rlshift__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other<<self."
        return self.__op2(operator.lshift, other, self)

    def __rmod__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other%self."
        return self.__op2(operator.mod, other, self)

    def __rmul__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other*self."
        return self.__op2(operator.mul, other, self)

    def __ror__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other|self."
        return self.__op2(operator.or_, other, self)

    def __rpow__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other**self."
        return self.__op2(operator.pow, other, self)

    def __rrshift__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other>>self."
        return self.__op2(operator.rshift, other, self)

    def __rsub__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other-self."
        return self.__op2(operator.sub, other, self)

    def __rxor__(self: Self, other: SupportsInt, /) -> Self:
        "This magic method implements other^self."
        return self.__op2(operator.xor, other, self)
