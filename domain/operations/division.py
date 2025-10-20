from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers, require_nonzero_divisors


class Division(Operation):
    """Divide the first operand by subsequent operands in order.

    Requires at least one operand. With one operand, returns it.
    Raises ZeroDivisionError if any divisor is zero.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Division")
        require_numbers(operands, "Division")
        if len(operands) > 1:
            require_nonzero_divisors(operands[1:], "Division")

        it = iter(float(x) for x in operands)
        result = float(next(it))
        for divisor in it:
            result /= divisor
        return result
