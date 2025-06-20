# Write a Python program to merge two lists into one dictionary using a loop.



keys = ["name", "age", "city"]
values = ["Ravi", 25, "Delhi"]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Merged Dictionary:", d)
