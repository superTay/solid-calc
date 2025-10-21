from __future__ import annotations

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers
from ..validation.errors import InvalidValueError


class Sqrt(Operation):
    """Square root operation (unary or n-ary composing roots left-to-right).

    - With one operand: sqrt(x)
    - With many: sqrt(sqrt(...sqrt(x) ...)) applying sequentially
    - Rejects negative inputs at each step
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Sqrt")
        require_numbers(operands, "Sqrt")
        import math

        it = iter(float(x) for x in operands)
        value = float(next(it))
        if value < 0:
            raise InvalidValueError("Sqrt requires non-negative numbers")
        result = math.sqrt(value)
        for _ in it:
            # For additional operands, treat them as chaining sqrt
            if result < 0:
                raise InvalidValueError("Sqrt requires non-negative numbers")
            result = math.sqrt(result)
        return result

