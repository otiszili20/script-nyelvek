import secret_logic


def ask():
    print("calculator application. please give me the  ")

    print("1.operand (integer)")
    text = input()
    while not secret_logic.is_numeric(text):
        print("bad input, try again")
        text = input()
    operand1 = int(text)

    print("operator (+ | - | * | /)")
    text = input()
    while not secret_logic.is_supported_operator(text):
        print("bad input, try again")
        text = input()
    l_operator = text

    print("2.operand (integer)")
    text = input()
    while not secret_logic.is_numeric(text):
        print("bad input, try again")
        text = input()
    operand2 = int(text)

    return operand1, l_operator, operand2


op1, operator, op2 = ask()
result = secret_logic.calculate(op1, operator, op2)
print(f"result: {result}")
exit(0)
