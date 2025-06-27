"""Write a Python program to check the current position of the file cursor using tell().
"""





filename = "my_file.txt"

try:
    with open(filename, "r") as file:

        file.read(10)
        
        position = file.tell()

        print(f"Current file cursor position: {position}")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")