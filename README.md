# Solid Calc

Calculadora modular que aplica los patrones Strategy (operaciones) y Factory (creación por símbolo), con validación de dominio, servicio de aplicación y un CLI simple.

## UI (Tkinter)
- Requisitos: Python 3.11+ y Tkinter (suele venir con Python estándar).
- Ejecutar:
  - Activar entorno: `conda activate <ENV_NAME>`
  - Lanzar: `python ui/app.py`

Arquitectura UI:
- UI: `ui/app.py` (ventana Tkinter con display y keypad).
- Evaluador: `domain/evaluator.py` parsea expresiones simples y delega a operaciones mediante `OperationFactory`.
- Operaciones de dominio: `domain/operations/*` (`Addition`, `Substraction`, `Multiplication`, `Division`) implementan `execute(*operands)`.

## Extended Operations (English)
New domain operations have been added and are available through the evaluator and factory:
- Power (`^`): `domain/operations/power.py` — supports n-ary left-to-right exponentiation, e.g. `2^3^2`.
- Square root (`sqrt`): `domain/operations/sqrt.py` — unary, chainable. Accepts `sqrt 9` or `sqrt(16)`. Negative values raise an error.

How to try them:
- UI: launch `python ui/app.py` and type `2^3`, `2^3^2`, `sqrt 9`, `sqrt(16)`.
- CLI (service-based): `python -m application.cli '^' 2 3` or `python -m application.cli sqrt 9`.

Design notes:
- The UI remains decoupled and delegates to `domain/evaluator.py`.
- `domain/factory/operation_factory.py` registers symbols `^` and `sqrt` and returns the appropriate operation classes.
- Validations reuse existing domain validators (arity, numbers); sqrt rejects negative inputs.

## Estructura
- `domain/`
  - `operations/`: interfaz `Operation` y estrategias (`Addition`, `Substraction`, `Multiplication`, `Division`).
  - `validation/`: errores de dominio y validadores reutilizables.
  - `factory/`: `OperationFactory` que crea operaciones a partir de símbolos (`+ - * /`).
- `application/`
  - `services/`: `CalculatorService`, orquesta el cálculo con la fábrica.
  - `cli.py`: CLI con `argparse`.
- `tests/`: pruebas de smoke para service/factory y CLI.

## Instalación (entorno sugerido)
```bash
conda create -n calc-env python=3.11 -y
conda activate calc-env
pip install -e .
```

Herramientas opcionales (recomendadas):
```bash
pip install pytest ruff mypy
```

## Uso (CLI)
Tras `pip install -e .`, se instala el comando `calc`.

```bash
# suma
calc + 1 2 3        # => 6.0

# multiplicación (escapar *)
calc '*' 4 5        # => 20.0
# o
calc \* 4 5

# división con error
calc / 5 0          # => exit code 1, "Division by zero"
```

También puedes invocarlo por módulo sin instalar el script:
```bash
python -m application.cli + 1 2 3
python -m application.cli '*' 4 5
```

## Uso (como librería)
```python
from application.services.calculator_service import CalculatorService

svc = CalculatorService()
print(svc.calculate("+", 1, 2, 3))   # 6.0
print(svc.calculate("/", 20, 2, 2))  # 5.0
```

## Tests
```bash
pytest
```

## Calidad
```bash
ruff check . && ruff format .
mypy .
```

## Próximos pasos
- Añadir más operaciones (potencia, módulo, media) y registrarlas en la factory.
- CLI interactivo (REPL) o interfaz gráfica opcional.
- Abrir Pull Request desde `feature/ui` hacia `main` cuando la UI esté validada.
- Ejemplos avanzados y casos de uso en el README.
