from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Substraction(Operation):
    """Subtract numbers in order: start with the first, minus the rest.

    Easy explanation:
    - With one number, the answer is that number.
    - With many numbers, we do: first - second - third - ...
    - If no numbers are given, we raise a clear error.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Substraction")
        require_numbers(operands, "Substraction")
        it = iter(float(x) for x in operands)
        result = float(next(it))
        for value in it:
            result -= value
        return result
