from warnings import warn
oper = "+-/*"
def to_infix_notation(expression: str) -> str:
    if not expression.strip():
        return ""
    tokens = expression.strip().split()
    stack = []
    for token in reversed(tokens):
        if token in oper:
            if len(stack) < 2:
                warn(f"Not enough operands for operator '{token}'")
                return ""
            left, right = stack.pop(), stack.pop()
            stack.append(f"({left} {token} {right})")
        else:
            stack.append(token)
    if len(stack) != 1:
        warn("There are extra operands")
    return stack[0][1:-1] if stack else ""
