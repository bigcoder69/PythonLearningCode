def calculator():
    # Get the first number
    first_number = int(input("Enter first number: "))
    # Get the second number
    second_number = int(input("Enter second number: "))
    # Get the operation
    operation = input("Enter operation: ")
    # Perform the calculation
    if operation == "+":
        print(first_number + second_number)
    
    elif operation == "-":
        print(first_number - second_number)

    elif operation == "*":
        print(first_number * second_number)

    elif operation == "/":
        print(first_number / second_number)

    else:
        print("Invalid operation")

# Run the calculator function forever
while True:
    calculator()

