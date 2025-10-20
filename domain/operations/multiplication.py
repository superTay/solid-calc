from __future__ import annotations

from .interface import Operation


class Multiplication(Operation):
    """Multiply all provided operands.

    Requires at least one operand.
    """

    def execute(self, *operands: float) -> float:
        if not operands:
            raise ValueError("Multiplication requires at least one operand")
        result = 1.0
        for value in operands:
            result *= float(value)
        return result

