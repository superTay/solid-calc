from __future__ import annotations

from typing import Iterable, Sequence

from .errors import InvalidArityError, InvalidValueError, DivisionByZeroError


Number = float | int


def require_at_least(operands: Sequence[Number], n: int, op_name: str) -> None:
    if len(operands) < n:
        raise InvalidArityError(f"{op_name} requires at least {n} operand(s)")


def require_numbers(operands: Iterable[object], op_name: str) -> None:
    for value in operands:
        if not isinstance(value, (int, float)):
            raise InvalidValueError(f"{op_name} expects numeric operands, got {type(value).__name__}")


def require_nonzero_divisors(divisors: Iterable[Number], op_name: str) -> None:
    for value in divisors:
        if float(value) == 0.0:
            raise DivisionByZeroError("Division by zero")

