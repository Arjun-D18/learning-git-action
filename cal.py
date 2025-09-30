# calculator.py
# A simple command-line calculator program written in Python.

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers, handling division by zero."""
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculator_cli():
    """Provides a simple interactive command-line interface for the calculator."""
    print("Simple Python CLI Calculator")
    print("----------------------------")

    while True:
        # Display menu and get user choice
        print("\nOperations:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Exit")

        choice = input("Enter operation number (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        result = None
        
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        # Print the result
        if result is not None:
            print(f"Result: {result}")

# Entry point for the application
if __name__ == "__main__":
    calculator_cli()
