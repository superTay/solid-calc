from __future__ import annotations


class CalculationError(Exception):
    """Base domain error for calculator operations."""


class InvalidArityError(CalculationError):
    """Raised when the number of operands is invalid."""


class InvalidValueError(CalculationError):
    """Raised when an operand value/type is invalid."""


class DivisionByZeroError(CalculationError, ZeroDivisionError):
    """Raised when attempting to divide by zero."""

