""""Write a Python program to demonstrate handling multiple exceptions."""


try:

    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    result = num1 / num2
    
    print(f"Result of {num1} / {num2} = {result}")

except ZeroDivisionError:
    print("Error: You can't divide by zero!")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")