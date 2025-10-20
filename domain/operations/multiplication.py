from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Multiplication(Operation):
    """Multiply all provided operands.

    Requires at least one operand.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Multiplication")
        require_numbers(operands, "Multiplication")
        result = 1.0
        for value in (float(x) for x in operands):
            result *= value
        return result
