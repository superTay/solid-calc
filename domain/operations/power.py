from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Power(Operation):
    """Exponentiation.

    Supports binary (base, exp) and n-ary left-to-right: (((a ** b) ** c) ...).
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Power")
        require_numbers(operands, "Power")
        it = iter(float(x) for x in operands)
        result = float(next(it))
        for exp in it:
            result = result ** float(exp)
        return result

