# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']



m = ['apple', 'banana', 'mango']

for i in m:
    if i == 'banana':
        continue  
    print(i)
