"""  Write a Python program to print custom exceptions."""




class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError()
    print(f"You entered: {num}")

except NegativeNumberError as nne:
    print(f"Custom Exception: {nne}")

except ValueError:
    print("Error: Please enter a valid integer.")