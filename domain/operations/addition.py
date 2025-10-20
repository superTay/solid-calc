from __future__ import annotations

from typing import Iterable

from .interface import Operation


class Addition(Operation):
    """Sum all provided operands.

    Requires at least one operand.
    """

    def execute(self, *operands: float) -> float:
        if not operands:
            raise ValueError("Addition requires at least one operand")
        return float(sum(operands))

