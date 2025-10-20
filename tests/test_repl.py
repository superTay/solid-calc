from __future__ import annotations

from io import StringIO

from application.repl import repl


def run(lines: list[str]):
    inp = StringIO("\n".join(lines) + "\n")
    out = StringIO()
    err = StringIO()
    code = repl(stdin=inp, stdout=out, stderr=err)
    return code, out.getvalue(), err.getvalue()


def test_repl_happy_path_and_exit():
    code, out, err = run(["+ 1 2 3", "exit"])
    assert code == 0
    assert "6.0" in out
    assert err == ""


def test_repl_error_division_by_zero():
    code, out, err = run(["/ 5 0", "quit"])
    assert code == 0
    assert "Error: Division by zero" in err

