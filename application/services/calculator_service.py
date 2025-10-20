from __future__ import annotations

from typing import Iterable

from domain.factory.operation_factory import OperationFactory


class CalculatorService:
    """Application service that delegates operation creation to the factory."""

    def __init__(self, factory: OperationFactory | None = None) -> None:
        self._factory = factory or OperationFactory()

    def calculate(self, symbol: str, *operands: float) -> float:
        operation = self._factory.create(symbol)
        return operation.execute(*operands)
