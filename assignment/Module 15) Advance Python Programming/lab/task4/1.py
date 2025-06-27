# Write a Python program to read the contents of a file and print them on the console.


filename = "output.txt"

try:

    with open(filename, "r") as file:
        contents = file.read()

    print("File contents:")
    print(contents)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")



print("\nnext program.....")
print()
