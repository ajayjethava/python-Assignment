"""Write a Python program to create a file and print the string into the
file. """




filename = "my_file.txt"

text = "This string will be written to the file."

with open(filename, "w") as file:
    file.write(text)

print(f"The text has been written to '{filename}'.")


print()
print()






