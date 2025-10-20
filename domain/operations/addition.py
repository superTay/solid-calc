from __future__ import annotations

from typing import Iterable

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Addition(Operation):
    """Add numbers together and return the total.

    Easy explanation:
    - Give me 1 or more numbers and I will sum them.
    - If you forget to pass numbers, I will raise a clear error.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Addition")
        require_numbers(operands, "Addition")
        return float(sum(float(x) for x in operands))