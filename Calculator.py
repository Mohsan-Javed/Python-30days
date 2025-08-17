op = ""
while op != "q":
    op = input(f"Please enter your operator (+ for add, - for subtract, * for multiply, / for divide, ** for square, Press 'q' to quit): ")
    if op == "q":
        print("Goodbye!")
        break
    match op:
        case "+" :
            num1 = int(input(f"Please enter your first number: "))
            num2 = int(input(f"Please enter your second number: "))
            result = num1 + num2
            print(round(result, 2))
        case "-" :
            num1 = int(input(f"Please enter your first number: "))
            num2 = int(input(f"Please enter your second number: "))
            result = num1 - num2
            print(round(result, 2))
        case "*" :
            num1 = int(input(f"Please enter your first number: "))
            num2 = int(input(f"Please enter your second number: "))
            result = num1 * num2
            print(round(result, 2))
        case "/" :
            num1 = int(input(f"Please enter your first number: "))
            num2 = int(input(f"Please enter your second number: "))
            result = num1 / num2
            print(round(result, 2))
        case ("**"):
            num1 = int(input(f"Please enter your base number: "))
            num2 = int(input(f"Please enter your power: "))
            result = num1 ** num2
            print(round(result, 2))
        case _ :
            print(f"{op} is not a valid operator")