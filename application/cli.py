from __future__ import annotations

import argparse
import sys
from typing import List

from domain.validation.errors import (
    CalculationError,
    DivisionByZeroError,
    InvalidArityError,
    InvalidValueError,
)
from application.services.calculator_service import CalculatorService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc",
        description="Simple calculator using Strategy + Factory patterns",
    )
    parser.add_argument("symbol", type=str, help="Operation symbol: + - * /")
    parser.add_argument(
        "operands",
        metavar="N",
        type=float,
        nargs=argparse.ONE_OR_MORE,
        help="Numeric operands (space-separated)",
    )
    return parser


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    service = CalculatorService()
    try:
        result = service.calculate(args.symbol, *args.operands)
        print(result)
        return 0
    except DivisionByZeroError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except (InvalidArityError, InvalidValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    except CalculationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())

