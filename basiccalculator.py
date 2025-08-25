
# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for operation
operation = input("Enter an operation (Addition,Subtraction,Multiplication,Division): ")

# Perform calculation
if operation == "Addition":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "Subtraction":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "Multiplication":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose Addition, Subtraction,Multiplication, or Division.")

