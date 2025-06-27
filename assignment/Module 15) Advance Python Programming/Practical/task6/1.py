"""Write a Python program to create a class and access the properties
of the class using an object."""


class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

my_car = Car("Toyota", "Corolla")

print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")



print()
print()
