from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Multiplication(Operation):
    """Multiply numbers together and return the product.

    Easy explanation:
    - Start with 1, then multiply by each number in order.
    - Needs at least one number or we raise a clear error.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Multiplication")
        require_numbers(operands, "Multiplication")
        result = 1.0
        for value in (float(x) for x in operands):
            result *= value
        return result
