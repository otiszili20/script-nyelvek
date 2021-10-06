print("calculator application. please give me the  ")

print("1.operand")
operand1 = int(input())

print("operator")
operator = input()

print("2.operand")
operand2 = int(input())

if operator == "+":
    result = operand1 + operand2

print(f"result: {result}")
exit(0)
