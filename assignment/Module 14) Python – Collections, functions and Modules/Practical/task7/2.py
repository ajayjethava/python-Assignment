#  16) Write a Python program to separate keys and values from a dictionary using 
#      keys() and values() methods.




student = {
    "name": "rohan",
    "grade": "A",
    "marks": 85
}

keys = student.keys()
values = student.values()

print("keys:", list(keys))
print("values:", list(values))
