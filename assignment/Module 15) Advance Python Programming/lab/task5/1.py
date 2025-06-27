# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).


try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
    
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator.")

    print(f"Result: {result}")

except ValueError as ve:
    print("ValueError:", ve)

except ZeroDivisionError as zde:
    print("ZeroDivisionError:", zde)

except Exception as e:
    print("An unexpected error occurred:", e)


print()
print()


