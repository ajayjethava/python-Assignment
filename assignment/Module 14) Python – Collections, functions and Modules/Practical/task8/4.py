#  22) Write a Python program to create a lambda function with two expressions.





calc = lambda x: (x**2, x**3)

square, cube = calc(3)
print("Square:", square)
print("Cube:", cube)