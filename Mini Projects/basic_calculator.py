def calculator():
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print(f"{operator} is not a valid operator.")
        result = None
    return (round(result,2))

operator = input ("Enter an operator (+, -, *, %, /): ")
num1 = float(input("Enter first number: ")) # Typecasting input to float or int for decimal support
num2 = float(input("Enter second number: "))

print("The result is: ", calculator())