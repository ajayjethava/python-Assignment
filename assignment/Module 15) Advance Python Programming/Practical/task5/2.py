"""Write a Python program to handle multiple exceptions (e.g., file not found, division by zero)."""




try:
    filename = input("Enter filename to read: ")
    with open(filename, 'r') as file:
        data = file.read()
        print("File content:")
        print(data)
    
    x = int(input("Enter a number to divide 10 by: "))
    result = 10 / x
    print(f"Result: {result}")

except FileNotFoundError:
    print("Error: File not found!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input!")

except Exception as e:
    print(f"Unexpected error: {e}")



print()
print("next program....")
print()