from __future__ import annotations

from typing import Callable, Dict, Type

from ..operations.interface import Operation
from ..operations.addition import Addition
from ..operations.substraction import Substraction
from ..operations.multiplication import Multiplication
from ..operations.division import Division
from ..validation.errors import InvalidValueError


class OperationFactory:
    """Create operation objects from a simple text symbol.

    Plain-English idea:
    - You give me a symbol like "+" or "*".
    - I look up which class does that math.
    - I build it and hand it back to you.

    Why this is helpful:
    - The rest of the program doesn't need "if symbol == '+'" chains.
    - Adding a new operation is as easy as registering it once.
    """

    def __init__(self) -> None:
        self._registry: Dict[str, Callable[[], Operation]] = {
            "+": Addition,
            "-": Substraction,
            "*": Multiplication,
            "/": Division,
        }

    def register(self, symbol: str, builder: Callable[[], Operation]) -> None:
        """Connect a new symbol with a function/class that builds an operation.

        Example:
            factory.register("^", Power)

        Later, ``factory.create("^")`` will return ``Power()``.
        """
        if not symbol or not isinstance(symbol, str):
            raise InvalidValueError("Symbol must be a non-empty string")
        self._registry[symbol] = builder

    def create(self, symbol: str) -> Operation:
        """Build the operation that matches ``symbol``.

        Raises:
            InvalidValueError: if the symbol is unknown.
        """
        try:
            builder = self._registry[symbol]
        except KeyError as exc:
            raise InvalidValueError(f"Unknown operation symbol: {symbol!r}") from exc
        return builder()
