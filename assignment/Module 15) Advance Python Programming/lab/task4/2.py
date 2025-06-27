# Write a Python program to write multiple strings into a file.



filename = "multiline_output.txt"

lines = [
    "First line of text.",
    "Second line of text.",
    "Third line of text."
]

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")  

print(f"{len(lines)} lines have been written to '{filename}'.")