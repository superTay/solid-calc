from __future__ import annotations

from typing import Iterable

from domain.factory.operation_factory import OperationFactory


class CalculatorService:
    """High-level calculator that asks a factory for the right operation.

    Kid-friendly story of what happens:
    - You say which math you want (the symbol) and the numbers.
    - The service asks the factory to build the right operation object.
    - It runs that operation with your numbers and returns the answer.

    This keeps the code clean:
    - No big "if/elif" chains for "+, -, *, /" here.
    - New operations can be added in one place (the factory) and work everywhere.
    """

    def __init__(self, factory: OperationFactory | None = None) -> None:
        """Optionally receive a pre-made factory (useful for testing).

        If not provided, a default ``OperationFactory`` is created.
        """
        self._factory = factory or OperationFactory()

    def calculate(self, symbol: str, *operands: float) -> float:
        """Compute the result of the chosen operation with the given numbers.

        Example:
            calculate("+", 1, 2, 3) -> 6.0
        """
        operation = self._factory.create(symbol)
        return operation.execute(*operands)
