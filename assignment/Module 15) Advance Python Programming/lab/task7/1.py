"""Write Python programs to demonstrate different types of inheritance (single, multiple,
multilevel, etc.)."""


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  
dog.bark()

print()
print("next....")
print()

class Father:
    def skills(self):
        print("Father has gardening skills")

class Mother:
    def skills(self):
        print("Mother has cooking skills")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child has combined skills")

child = Child()
child.skills()



print()
print("next....")
print()


class Grandparent:
    def heritage(self):
        print("Grandparent's heritage")

class Parent(Grandparent):
    def skills(self):
        print("Parent's skills")

class Child(Parent):
    def hobbies(self):
        print("Child's hobbies")

c = Child()

c.heritage() 
c.skills()   
c.hobbies()   


print()
print("next....")
print()


class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()



print()
print("next....")
print()


class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()