from domain.factory.operation_factory import OperationFactory


def evaluate_expression(expr: str):
    expr = expr.strip()
    if not expr:
        raise ValueError("Empty expression")

    # Addition n-aria: separar por '+' y pasar todos los operandos
    if '+' in expr:
        parts = [p.strip() for p in expr.split('+') if p.strip()]
        numbers = [float(p) for p in parts]
        op = OperationFactory().create('+')
        return op.execute(*numbers)

    # Potencia '^' (binario o n-ario izquierda->derecha)
    if '^' in expr:
        parts = [p.strip() for p in expr.split('^') if p.strip()]
        numbers = [float(p) for p in parts]
        op = OperationFactory().create('^')
        return op.execute(*numbers)

    # Raíz cuadrada: soporta forma textual 'sqrt NUM' o 'sqrt(NUM)'
    if expr.startswith('sqrt'):
        inside = expr[4:].strip()
        if inside.startswith('(') and inside.endswith(')'):
            inside = inside[1:-1].strip()
        tokens = [t for t in inside.replace(',', ' ').split() if t]
        if not tokens:
            raise ValueError("sqrt requires at least one operand")
        numbers = [float(t) for t in tokens]
        op = OperationFactory().create('sqrt')
        return op.execute(*numbers)

    # Operadores binarios: '-', '*', '/'
    for symbol in ('-', '*', '/'):
        if symbol in expr:
            left, right = expr.rsplit(symbol, 1)
            a = float(left.strip())
            b = float(right.strip())
            op = OperationFactory().create(symbol)
            return op.execute(a, b)

    # Sin operador, es un número
    return float(expr)
