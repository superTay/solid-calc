from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Substraction(Operation):
    """Subtract subsequent operands from the first.

    Requires at least one operand. With one operand, returns it.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Substraction")
        require_numbers(operands, "Substraction")
        it = iter(float(x) for x in operands)
        result = float(next(it))
        for value in it:
            result -= value
        return result
