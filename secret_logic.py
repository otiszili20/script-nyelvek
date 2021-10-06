def is_numeric(text):
    return text.isnumeric()


def is_supported_operator(text):
    text in ['+', '-', '*', '/']


def calculate(operand1, p_operator, operand2):
    rv = 0
    if p_operator == "+":
        rv = operand1 + operand2
    elif p_operator == "-":
        rv = operand1 + operand2
    elif p_operator == "*":
        rv = operand1 * operand2
    elif p_operator == "/":
        rv = operand1 / operand2
    return rv
