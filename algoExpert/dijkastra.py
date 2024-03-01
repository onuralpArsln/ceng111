#  Dijkstra's Two-Stack Algorithm needs to be corrected tho 


def result(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b  # Corrected subtraction operation
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b  # Use integer division here
    else:
        raise ValueError(f"{op} is not a recognized operator.")

def evaluate(expr):
    ops = []
    values = []

    i = 0
    while i < len(expr):
        c = expr[i]
        if c == '(':
            ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(':
                values.append(result(ops.pop(), values.pop(), values.pop()))
            ops.pop()  # Discard '('
        elif c in ['+', '-', '*', '/']:
            while ops and precedence(ops[-1]) >= precedence(c):
                values.append(result(ops.pop(), values.pop(), values.pop()))
            ops.append(c)
        elif c.isdigit():
            # Extract the entire number using exponentiation
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 ** (len(expr[i:]) - 1) + int(expr[i])
                i += 1
            i -= 1  # Move back one step to handle the next character correctly
            values.append(num)
        i += 1

    while ops:
        values.append(result(ops.pop(), values.pop(), values.pop()))

    return values.pop()

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    else:
        return 0

expression = "(3+4)*5-(6/2)"
result = evaluate(expression)
print("Result:", result)
