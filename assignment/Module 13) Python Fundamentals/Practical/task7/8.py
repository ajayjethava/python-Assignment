#   Practical Example: 8) Write a Python program to print a string from the last character.




def fun(m):
    for i in reversed(m):
        print(i, end='')

a = input("Enter a string: ")
fun(a)
