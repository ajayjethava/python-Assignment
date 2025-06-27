"""Write a Python program to handle file exceptions and use the finally block for closing
the file. """



filename = "example.txt"

try:
    file = open(filename, "r")
    content = file.read()
    print("File contents:")
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist!")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        
        print("File was never opened, so no need to close.")


print()
print("next program ....")
print()