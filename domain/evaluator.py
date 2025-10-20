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
