from __future__ import annotations

from .interface import Operation


class Division(Operation):
    """Divide the first operand by subsequent operands in order.

    Requires at least one operand. With one operand, returns it.
    Raises ZeroDivisionError if any divisor is zero.
    """

    def execute(self, *operands: float) -> float:
        if not operands:
            raise ValueError("Division requires at least one operand")
        it = iter(operands)
        result = float(next(it))
        for value in it:
            divisor = float(value)
            if divisor == 0.0:
                raise ZeroDivisionError("Division by zero")
            result /= divisor
        return result

