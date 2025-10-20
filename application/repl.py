from __future__ import annotations

import sys

from application.services.calculator_service import CalculatorService
from domain.validation.errors import (
    CalculationError,
    DivisionByZeroError,
    InvalidArityError,
    InvalidValueError,
)


PROMPT = "calc> "
HELP = (
    "Enter operations as: <symbol> <op1> <op2> [...].\n"
    "Examples: + 1 2 3 | / 20 2 2 | '*' 4 5 (quote * in shells).\n"
    "Commands: help, quit, exit"
)


def parse_line(line: str) -> tuple[str, list[float]]:
    parts = line.strip().split()
    if not parts:
        raise InvalidValueError("Empty input")
    symbol = parts[0]
    try:
        operands = [float(x) for x in parts[1:]]
    except ValueError as exc:
        raise InvalidValueError("All operands must be numeric") from exc
    return symbol, operands


def repl(stdin=None, stdout=None, stderr=None) -> int:
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr

    service = CalculatorService()
    print(HELP, file=stdout)

    while True:
        try:
            print(PROMPT, end="", file=stdout, flush=True)
            line = stdin.readline()
            if not line:
                break  # EOF
            line = line.strip()
            if not line:
                continue
            if line in {"quit", "exit"}:
                break
            if line == "help":
                print(HELP, file=stdout)
                continue

            symbol, operands = parse_line(line)
            result = service.calculate(symbol, *operands)
            print(result, file=stdout)
        except DivisionByZeroError as e:
            print(f"Error: {e}", file=stderr)
        except (InvalidArityError, InvalidValueError) as e:
            print(f"Error: {e}", file=stderr)
        except CalculationError as e:
            print(f"Error: {e}", file=stderr)

    return 0


def main() -> int:
    return repl()


if __name__ == "__main__":
    raise SystemExit(main())

