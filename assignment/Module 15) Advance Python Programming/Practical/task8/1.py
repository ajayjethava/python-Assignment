"""Write a Python program to show method overloading."""

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


    def add_multiple(self, *numbers):
        return sum(numbers)

calc = Calculator()

print(calc.add(5, 10))         
print(calc.add(5, 10, 15))     
print(calc.add_multiple(1, 2, 3, 4, 5))  


print()
print("next ..")
print()


