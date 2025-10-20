from __future__ import annotations

import sys
from subprocess import run, PIPE


def run_cli(*args: str):
    proc = run([sys.executable, "-m", "application.cli", *args], stdout=PIPE, stderr=PIPE, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def test_cli_addition():
    code, out, err = run_cli("+", "1", "2", "3")
    assert code == 0
    assert out == "6.0"
    assert err == ""


def test_cli_division_by_zero():
    code, out, err = run_cli("/", "5", "0")
    assert code == 1
    assert out == ""
    assert "Division by zero" in err


def test_cli_unknown_symbol():
    code, out, err = run_cli("?", "1", "2")
    assert code == 2
    assert out == ""
    assert "Unknown operation symbol" in err

