"""Write a Python program to create a file and write a string into it."""







filename = "output.txt"

text_to_write = "This is a string written to the file."

with open(filename, "w") as file:
    file.write(text_to_write)

print(f"The string has been written to '{filename}'.")