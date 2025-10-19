from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable, Any


class Operation(ABC):
    """Abstract interface for calculator operations.

    Concrete operations (e.g., Add, Subtract) should implement `execute`.
    Keep implementations stateless when possible.
    """

    @abstractmethod
    def execute(self, *operands: float) -> float:
        """Execute the operation and return the result.

        - Accepts one or more numeric operands.
        - Should raise ValueError for invalid arity or values.
        """
        raise NotImplementedError


@runtime_checkable
class OperationProtocol(Protocol):
    """Duck-typed protocol variant of Operation.

    Useful for structural typing in places where inheritance
    from `Operation` is undesirable.
    """

    def execute(self, *operands: float) -> float:  # pragma: no cover - signature only
        ...
