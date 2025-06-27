"""Write a Python program to demonstrate the use of super() in inheritance."""




class Parent:
    def __init__(self):
        print("Parent constructor called")

    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()  
        print("Child constructor called")

    def greet(self):
        super().greet()  
        print("Hello from Child")

child = Child()
child.greet()