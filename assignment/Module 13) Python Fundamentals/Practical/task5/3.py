#  Practical Example 3: Write a Python program to find a specific string in the list using a simple
#  for loop and if condition.




my_list = ["apple", "banana", "cherry", "date"]


search_string = "banana"

found = False

for item in my_list:
    if item == search_string:
        found = True
        break 

if found:
    print(" is present in the list.",search_string)
else:
    print("is not present in the list.",search_string)
