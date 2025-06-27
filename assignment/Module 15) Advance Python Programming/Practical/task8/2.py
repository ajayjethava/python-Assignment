""" Write a Python program to show method overriding."""



class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):

    def move(self):
        print("Car is driving")


v = Vehicle()
v.move()  

c = Car()
c.move()  