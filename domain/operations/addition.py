from __future__ import annotations

from typing import Iterable

from .interface import Operation
from ..validation.validators import require_at_least, require_numbers


class Addition(Operation):
    """Sum all provided operands.

    Requires at least one operand.
    """

    def execute(self, *operands: float) -> float:
        require_at_least(operands, 1, "Addition")
        require_numbers(operands, "Addition")
        return float(sum(float(x) for x in operands))
