"""Write a Python program to handle exceptions in a calculator."""


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator!")

    print(f"Result: {result}")

except ZeroDivisionError as zde:
    print(f"Error: {zde}")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Unexpected error: {e}")



print()
print("next program ....")
print()























