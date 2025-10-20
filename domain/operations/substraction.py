from __future__ import annotations

from .interface import Operation


class Substraction(Operation):
    """Subtract subsequent operands from the first.

    Requires at least one operand. With one operand, returns it.
    """

    def execute(self, *operands: float) -> float:
        if not operands:
            raise ValueError("Substraction requires at least one operand")
        it = iter(operands)
        result = float(next(it))
        for value in it:
            result -= float(value)
        return result

