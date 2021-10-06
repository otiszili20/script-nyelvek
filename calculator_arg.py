import sys

import secret_logic


def print_usage_and_exit():
    print("calculator app. usage: OPERAND OPERATOR OPERAND. f.e 3 + 4")
    exit(-1)


if len(sys.argv) != 4:
    print_usage_and_exit()

op1 = int(sys.argv[1])
operator = sys.argv[2]
op2 = int(sys.argv[1])

result = secret_logic.calculate(op1, operator, op2)
print(f"result: {result}")
exit(0)
