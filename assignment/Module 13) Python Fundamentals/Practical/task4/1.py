#   Practical Example 5: Write a Python program to find greater and less than a number using
#    if_else.





num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(num1," is greater than ",num2)
elif num1 < num2:
    print(num1,"is less than ",num2)
else:
    print(num1 ,"is equal to", num2)
