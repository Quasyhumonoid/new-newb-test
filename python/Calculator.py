num1 = float(input("enter the number1 "))
num2 = float(input("enter the number2 "))
op = input("enter operator +, -, *, /")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
