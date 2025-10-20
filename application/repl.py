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
    """Turn one input line into a symbol and a list of numbers.

    Think of the line like a sentence: the first word is the action
    (the math symbol), and the next words are the numbers.

    Example: "+ 1 2 3" -> ("+", [1.0, 2.0, 3.0])

    - If the line is empty, we say it's not valid.
    - If a number can't be understood (e.g., "abc"), we raise a clear error.
    """
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
    """A tiny interactive calculator loop (REPL).

    How it works, in kid-friendly terms:
    1) We show a help message so you know what to type.
    2) We show a prompt like "calc> " and wait for you to write something.
    3) You write a math symbol and some numbers, like "+ 1 2 3".
    4) We read your line, split it into the symbol and numbers, and do the math.
    5) We print the answer. Then we go back to step 2 and repeat.
    6) If you type "exit" or "quit", we stop politely.

    Special commands:
    - help: prints the short instructions again.
    - exit/quit: leaves the calculator.

    Errors (like dividing by zero or typing a word instead of a number)
    are caught and printed as friendly messages so the loop can continue.
    """
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr

    service = CalculatorService()
    print(HELP, file=stdout)

    while True:
        try:
            # Show the prompt and flush so it appears immediately.
            print(PROMPT, end="", file=stdout, flush=True)
            line = stdin.readline()
            if not line:
                break  # End-of-file (Ctrl+D). We exit the loop.
            line = line.strip()
            if not line:
                continue  # Empty line: ask again.
            if line in {"quit", "exit"}:
                break
            if line == "help":
                print(HELP, file=stdout)
                continue

            # Turn the text into a symbol and a list of numbers.
            symbol, operands = parse_line(line)
            # Ask the service to do the math.
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
    """Program entry: start the REPL using the real stdin/stdout/stderr."""
    return repl()


if __name__ == "__main__":
    raise SystemExit(main())
