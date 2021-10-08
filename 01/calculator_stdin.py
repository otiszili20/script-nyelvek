import sys

import secret_logic


def print_usage_and_exit():
    print("calculator app. usage: OPERAND OPERATOR OPERAND. f.e. 3 + 4")
    exit(-1)


# "3 + 4"
def process_one_row(row):
    parts = row.split()
    if len(parts) != 3:
        print_usage_and_exit()

    if not secret_logic.is_numeric(parts[0]):
        print_usage_and_exit()
    op1 = int(parts[0])

    if not secret_logic.is_supported_operator(parts[1]):
        print_usage_and_exit()
    l_operator = parts[1]

    if not secret_logic.is_numeric(parts[2]):
        print_usage_and_exit()
    op2 = int(parts[2])

    return op1, l_operator, op2


def get_inputs():
    for row in sys.stdin:
        operand1, operator, operand2 = process_one_row(row)
        result = secret_logic.calculate(operand1, operator, operand2)
        print(f"result: {result}")


get_inputs()
exit(0)
