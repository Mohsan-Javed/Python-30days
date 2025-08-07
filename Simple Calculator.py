op = input(f"Please enter your operator (+, -, *, /): ")
num1 = int(input(f"Please enter your first number: "))
num2 = int(input(f"Please enter your second number: "))

if op == "+":
    result = num1 + num2
    print(round(result, 2))
elif op == "-":
    result = num1 - num2
    print(round(result, 2))
elif op == "*":
    result = num1 * num2
    print(round(result, 2))
elif op == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{op} is not a valid operator")
# the round() function rounds off a number to the desired count