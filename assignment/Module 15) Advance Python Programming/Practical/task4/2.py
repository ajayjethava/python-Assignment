""" Write a Python program to read a file and print the data on the console.s"""




filename = "my_file.txt"

try:
    with open(filename, "r") as file:
        data = file.read()
    
    print("File contents:")
    print(data)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")



print()
print()