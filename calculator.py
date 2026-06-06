def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    operation = input("What operation? (+, -, *, /): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = add(num1, num2)

    elif operation == "-":
        result = subtract(num1, num2)

    elif operation == "*":
        result = multiply(num1, num2)

    elif operation == "/":
        result = divide(num1, num2)

    else:
        result = "Invalid operation"

    print("Result:", result)

    again = input("Do you want to continue? (yes/no): ")

    if again == "no":
        break