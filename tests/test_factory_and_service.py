from __future__ import annotations

import pytest

from domain.factory.operation_factory import OperationFactory
from application.services.calculator_service import CalculatorService
from domain.validation.errors import InvalidValueError, DivisionByZeroError


def test_factory_creates_default_operations():
    factory = OperationFactory()
    assert factory.create("+").execute(1, 2, 3) == 6.0
    assert factory.create("-").execute(10, 3, 2) == 5.0
    assert factory.create("*").execute(2, 3, 4) == 24.0
    assert factory.create("/").execute(20, 2, 2) == 5.0


def test_factory_unknown_symbol():
    factory = OperationFactory()
    with pytest.raises(InvalidValueError):
        factory.create("?")


def test_service_calculate_happy_paths():
    svc = CalculatorService()
    assert svc.calculate("+", 1, 2, 3) == 6.0
    assert svc.calculate("-", 10, 3, 2) == 5.0
    assert svc.calculate("*", 2, 3, 4) == 24.0
    assert svc.calculate("/", 20, 2, 2) == 5.0


def test_service_division_by_zero():
    svc = CalculatorService()
    with pytest.raises(DivisionByZeroError):
        svc.calculate("/", 5, 0)

