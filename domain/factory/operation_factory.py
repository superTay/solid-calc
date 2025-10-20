from __future__ import annotations

from typing import Callable, Dict, Type

from ..operations.interface import Operation
from ..operations.addition import Addition
from ..operations.substraction import Substraction
from ..operations.multiplication import Multiplication
from ..operations.division import Division
from ..validation.errors import InvalidValueError


class OperationFactory:
    """Factory to create `Operation` instances from a symbol.

    Supports registration to extend with new operations.
    """

    def __init__(self) -> None:
        self._registry: Dict[str, Callable[[], Operation]] = {
            "+": Addition,
            "-": Substraction,
            "*": Multiplication,
            "/": Division,
        }

    def register(self, symbol: str, builder: Callable[[], Operation]) -> None:
        if not symbol or not isinstance(symbol, str):
            raise InvalidValueError("Symbol must be a non-empty string")
        self._registry[symbol] = builder

    def create(self, symbol: str) -> Operation:
        try:
            builder = self._registry[symbol]
        except KeyError as exc:
            raise InvalidValueError(f"Unknown operation symbol: {symbol!r}") from exc
        return builder()

